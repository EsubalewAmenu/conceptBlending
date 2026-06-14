# Quantale-Theoretic Conceptual Blending

This submodule implements a robust, automated pipeline for extracting and blending conceptual representations using **Quantale theory**. It fuses fuzzy truth values (TruthValueQuantale) with structural symbolic axioms (LogicQuantale) to create a high-dimensional, context-aware representation called a **V-Predicate**.

## 🚀 Current Status: Phase 1 Completed

I have successfully moved from hardcoded/manual concepts to a learned extraction pipeline.

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
    - Replace synthetic training data in `gnn_trainer.py` with real **CSLB Concept Property Norms** (638 concepts).
2.  **Blending Engine Implementation**:
    - Fleshing out `quantale_colimit_engine.py` to implement the **Pushout** logic for blending two V-Predicates.
3.  **Optimization Loop**:
    - Implementing the `MacBride derivative` for automatic optimization of blend weights.
4.  **PeTTa Integration**:
    - Finalizing the serialization to MeTTa for full compatibility with the OpenCog Hyperon AtomSpace.

---

## 🏃 Quick Start for Mentor Review

> **All commands below must be run from the repo root:**
> ```bash
> cd ~/Desktop/conceptBlending
> ```

### 1. Setup Environment

Requires **Python 3.8+**. Install core dependencies:

```bash
pip3 install torch sentence-transformers requests pytest --break-system-packages
```

Install `torch-geometric`:

```bash
pip3 install torch-geometric --break-system-packages
```

> **Note**: `sentence-transformers` will automatically download the embedding model (~90MB) on first run.

---

### 2. Run the Test Suite

Verifies that all algebraic axioms (commutativity, residuation, ordering) hold:

```bash
cd ~/Desktop/conceptBlending
python3 -m pytest a_quantale_theoretic_approach/tests/test_truth_value_pipeline.py -v
```

Expected output:
```
test_truth_value_pipeline.py::TestTruthValuePipeline::test_ordering_sanity   PASSED
test_truth_value_pipeline.py::TestTruthValuePipeline::test_quantale_axioms   PASSED
test_truth_value_pipeline.py::TestTruthValuePipeline::test_reproducibility   PASSED
3 passed
```

---

### 3. Run the Extraction Demo

Runs the full pipeline (Embedding → GNN → Axiom Extraction → V-Predicate Assembly) for House, Diamond, and Fire:

```bash
cd ~/Desktop/conceptBlending
python3 -m a_quantale_theoretic_approach.demo_pipeline
```

Expected output (truth values may vary slightly):
```lisp
(= (VPredicate House expensive)   (ProductQuantale (Axiom_Default_Structural) 0.834))
(= (VPredicate House stationary)  (ProductQuantale (Axiom_Default_Structural) 0.854))
(= (VPredicate Diamond expensive) (ProductQuantale (Axiom_Default_Structural) 0.944))
(= (VPredicate Diamond hard)      (ProductQuantale (Axiom_Default_Structural) 0.946))
(= (VPredicate Fire hot)          (ProductQuantale (Axiom_Default_Structural) 0.917))
(= (VPredicate Fire dangerous)    (ProductQuantale (Axiom_Default_Structural) 0.919))
```

---

### 4. (Optional) Re-Train the GNN

If you wish to re-train the truth-value refinement model from scratch:

```bash
cd ~/Desktop/conceptBlending
python3 -m a_quantale_theoretic_approach.core_representation.gnn_trainer
```

Expected output:
```
Bootstrapping dataset...
Starting training...
Epoch 0: Loss 0.XXXX
Epoch 10: Loss 0.XXXX
Epoch 20: Loss 0.XXXX
Model saved to gnn_weights.pth
```

---

## 📝 Technical Notes

- **API Keys**: No API keys are required for Phase 1. `ConceptNet` queries use the public API, and embeddings use `sentence-transformers` (downloaded automatically on first run).
- **Weights**: Pre-trained weights are in `core_representation/gnn_weights.pth` and loaded automatically by the demo.
- **MeTTa**: The demo outputs `(= (VPredicate ...))` assertions compatible with the AtomSpace/PeTTa version.
- **Python**: Use `python3` (not `python`) on Linux systems where both Python 2 and 3 are installed.
