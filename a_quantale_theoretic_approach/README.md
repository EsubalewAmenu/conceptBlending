# Quantale-Theoretic Conceptual Blending

This submodule implements a robust, automated pipeline for extracting and blending conceptual representations using **Quantale theory**. It fuses fuzzy truth values (TruthValueQuantale) with structural symbolic axioms (LogicQuantale) to create a high-dimensional, context-aware representation called a **V-Predicate**.

## 🚀 Current Status: Phase 1 Completed

We have successfully moved from hardcoded/manual concepts to a learned extraction pipeline.

### ✅ Accomplishments
1.  **GNN-based Truth Value Extraction**:
    - Implemented `ConceptEmbedder` using `sentence-transformers` for context-aware property grounding.
    - Built a **Graph Attention Network (GAT)** (`QuantaleTruthValueGNN`) that refines property strengths based on their relation to the concept anchor.
    - Integrated mathematical constraints: All truth values are guaranteed to satisfy Quantale axioms (residuation, commutativity).
2.  **Logic Channel Integration**:
    - Established the symbolic extraction bridge from **ConceptNet** mapping semantic relations to LogicQuantale axioms.
3.  **Verification**:
    - 100% pass rate on algebraic and semantic ordering tests.
    - Baseline weights trained and saved in `gnn_weights.pth`.

---

## 🛠 Next Steps (After Review)

The following stages are planned to complete the full blending engine:

1.  **Semantic Property Discovery (Stage 2)**:
    - Replace mock property lists with an **LLM-based Zero-Shot extractor** to discover properties of arbitrary concepts autonomously.
2.  **Blending Engine Implementation**:
    - Fleshing out `quantale_colimit_engine.py` to implement the **Pushout** logic for blending two V-Predicates.
3.  **Optimization Loop**:
    - Implementing the `MacBride derivative` for automatic optimization of blend weights.
4.  **PeTTa Integration**:
    - Finalizing the serialization to MeTTa for full compatibility with the OpenCog Hyperon AtomSpace.

---

## 🏃 Quick Start for Mentor Review

To verify the extraction pipeline and see the Product Quantales in action:

### 1. Setup Environment
Ensure the dependencies are installed (requires Python 3.8+):
```bash
pip install -r a_quantale_theoretic_approach/requirements.txt
```

### 2. Run the Extraction Demo
This script runs the full pipeline (Embedding -> GNN -> Axiom Extraction -> V-Predicate Assembly):
```bash
python3 -m a_quantale_theoretic_approach.demo_pipeline
```

### 3. (Optional) Re-Train the GNN
If you wish to re-train the truth-value refinement model on the bootstrapping data:
```bash
python3 -m a_quantale_theoretic_approach.core_representation.gnn_trainer
```

## 📝 Technical Notes
- **API Keys**: No API keys are required for Phase 1. `ConceptNet` queries use the public API, and embeddings use `sentence-transformers` (downloaded automatically).
- **Weights**: Pre-trained weights are located in `core_representation/gnn_weights.pth`.
- **MeTTa**: The demo outputs `(= (VPredicate ...))` assertions compatible with the AtomSpace/PeTTa version.
