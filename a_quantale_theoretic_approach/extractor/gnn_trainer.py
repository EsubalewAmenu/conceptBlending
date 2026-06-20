import torch
import torch.nn.functional as F
from torch_geometric.loader import DataLoader
from .gnn_truth_value import QuantaleTruthValueGNN
from .concept_extractor import ConceptEmbedder, build_concept_graph

def train_quantale_gnn(
    model: QuantaleTruthValueGNN, 
    train_graphs: list, 
    epochs: int = 50, 
    lr: float = 0.001
):
    """
    Trains the GNN to produce Quantale-valid truth values.
    Targets are derived from Knowledge Graph weights (normalized to [0,1]).
    """
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for data in train_graphs:
            optimizer.zero_grad()
            
            # Predict truth values for all nodes
            pred_scores = model(data)
            
            # Target is in data.y (normalized KG weights)
            # We only train on property nodes (nodes 1..N), node 0 is the concept anchor
            # Masking can be applied here
            loss = F.mse_loss(pred_scores[1:], data.y[1:])
            
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss {total_loss/len(train_graphs):.4f}")

    return model

def bootstrap_training_data(embedder: ConceptEmbedder):
    """
    Creates a small synthetic dataset for bootstrapping.
    In production, this would fetch from ConceptNet.
    """
    raw_data = [
        ("House", {"expensive": 0.8, "safe": 0.9, "permanent": 0.85}),
        ("Diamond", {"expensive": 0.95, "hard": 1.0, "rare": 0.9}),
        ("Bird", {"flies": 0.9, "feathers": 1.0, "small": 0.6})
    ]
    
    graphs = []
    for concept, props in raw_data:
        graph = build_concept_graph(concept, props, embedder)
        graphs.append(graph)
    
    return graphs

if __name__ == "__main__":
    embedder = ConceptEmbedder(model_name="all-MiniLM-L6-v2")
    model = QuantaleTruthValueGNN(input_dim=384) # 384 for MiniLM
    
    print("Bootstrapping dataset...")
    train_data = bootstrap_training_data(embedder)
    
    print("Starting training...")
    trained_model = train_quantale_gnn(model, train_data, epochs=30)
    
    # Save the model
    torch.save(trained_model.state_dict(), "a_quantale_theoretic_approach/extractor/gnn_weights.pth")
    print("Model saved to gnn_weights.pth")
