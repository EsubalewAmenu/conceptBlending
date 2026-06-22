import torch
import torch.nn.functional as F
import os
import re
import random
import argparse
from typing import Dict, List, Tuple
from .gnn_truth_value import QuantaleTruthValueGNN
from .concept_extractor import ConceptEmbedder, build_concept_graph

def parse_metta_triples(file_path: str) -> List[Tuple[str, str, float]]:
    """Parses hasProperty triples from AtomSpace .metta files."""
    triples = []
    if not os.path.exists(file_path):
        return []
        
    # Pattern to match (hasProperty concept property) followed by (weight ... weight)
    # This is a simplified parser for the specific format seen in the zip
    with open(file_path, 'r') as f:
        content = f.read()
        
    # Find all hasProperty blocks
    # Format: (hasProperty concept property) ... (weight (...) weight)
    # We use a regex that looks for the relation and then captures the weight nearby
    pattern = r'\(hasProperty\s+([^\s\)]+)\s+([^\s\)]+)\).*?\(weight\s+\(hasProperty\s+\1\s+\2\)\s+([\d\.]+)\)'
    matches = re.finditer(pattern, content, re.DOTALL)
    
    for m in matches:
        concept = m.group(1).replace('_', ' ')
        prop = m.group(2).replace('_', ' ')
        weight = float(m.group(3))
        # Normalize weight: ConceptNet/CSLB weights usually go up to ~5.0. 
        # We normalize to [0,1] for the GNN sigmoid head.
        tv = min(weight / 5.0, 1.0) 
        triples.append((concept, prop, tv))
        
    return triples

def train_quantale_gnn(
    model: QuantaleTruthValueGNN, 
    train_graphs: list, 
    epochs: int = 50, 
    lr: float = 0.001,
    device: str = 'cpu'
):
    """
    Trains the GNN to produce Quantale-valid truth values with shuffling and clipping.
    """
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    
    for epoch in range(epochs):
        random.shuffle(train_graphs)
        total_loss = 0
        valid_graphs = 0
        
        model.train()
        for data in train_graphs:
            data = data.to(device)
            optimizer.zero_grad()
            
            pred_scores = model(data)
            # Node 0 is anchor, Node 1+ are properties
            loss = F.mse_loss(pred_scores[1:], data.y[1:])
            
            if torch.isnan(loss):
                continue
                
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            
            total_loss += loss.item()
            valid_graphs += 1
            
        if epoch % 5 == 0:
            print(f"Epoch {epoch}: Loss {total_loss/max(valid_graphs, 1):.4f} ({valid_graphs} graphs)")

    return model

def main():
    parser = argparse.ArgumentParser(description="Train Quantale GNN on AtomSpace data")
    parser.add_argument("--data_dir", type=str, help="Path to unzipped concept-atomspace folder")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--batch_size", type=int, default=200, help="Max concepts to build graphs for")
    args = parser.parse_args()

    # Configuration (Must match demo_pipeline.py)
    MODEL_NAME = "all-mpnet-base-v2"
    INPUT_DIM = 768
    
    embedder = ConceptEmbedder(model_name=MODEL_NAME)
    model = QuantaleTruthValueGNN(input_dim=INPUT_DIM)
    
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"Using device: {device}")

    if args.data_dir:
        print(f"Loading data from {args.data_dir}...")
        # Target the specific file that contains hasProperty
        prop_file = os.path.join(args.data_dir, "hasprerequisite-sw-hasproperty-as-hassubevent-bw-isa-ad.metta")
        triples = parse_metta_triples(prop_file)
        print(f"Loaded {len(triples)} triples.")
        
        # Group by concept
        concept_props = {}
        for c, p, tv in triples:
            if c not in concept_props: concept_props[c] = {}
            concept_props[c][p] = tv
            
        # Filter for quality
        filtered = {c: p for c, p in concept_props.items() if len(p) >= 3}
        print(f"Concepts with 3+ properties: {len(filtered)}")
        
        # Build graphs
        print(f"Building up to {args.batch_size} graphs (this takes time)...")
        train_data = []
        concepts = list(filtered.items())[:args.batch_size]
        for i, (concept, props) in enumerate(concepts):
            try:
                graph = build_concept_graph(concept, props, embedder)
                train_data.append(graph)
                if (i+1) % 20 == 0: print(f"  {i+1}/{len(concepts)} built...")
            except Exception as e:
                print(f"  Skipped {concept}: {e}")
    else:
        print("No data_dir provided. Using small bootstrap dataset.")
        from .gnn_trainer import bootstrap_training_data # In case of circularity or just local usage
        train_data = bootstrap_training_data(embedder)

    print("Starting training...")
    trained_model = train_quantale_gnn(model, train_data, epochs=args.epochs, device=device)
    
    # Save the model
    save_path = "a_quantale_theoretic_approach/extractor/gnn_weights.pth"
    torch.save(trained_model.state_dict(), save_path)
    print(f"Model saved to {save_path}")

def bootstrap_training_data(embedder: ConceptEmbedder):
    raw_data = [
        ("House", {"expensive": 0.16, "safe": 0.18, "permanent": 0.17}),
        ("Diamond", {"expensive": 0.20, "hard": 0.25, "rare": 0.19}),
        ("Fire", {"hot": 0.25, "dangerous": 0.30, "red": 0.28})
    ]
    return [build_concept_graph(c, p, embedder) for c, p in raw_data]

if __name__ == "__main__":
    main()

