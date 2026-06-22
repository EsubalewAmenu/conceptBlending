# Quantale-Theoretic Conceptual Blending Implementation

## Overview

The **Quantale-Theoretic Conceptual Blending** project implements a mathematically grounded framework for conceptual representation and blending. Unlike traditional flat data models, this approach utilizes **Quantale theory** to integrate fuzzy linguistic truth values with symbolic structural axioms, creating a context-aware representation known as a **V-Predicate**.

Phase 1 focus: **Automated Concept Extraction**. This phase automates the ingestion of conceptual properties and the refinement of their truth values using Graph Neural Networks (GNNs) grounded in real-world Knowledge Graphs.

## Setup and Run

### 1. Install Dependencies
Ensure you have Python 3.8+ installed. Install the required libraries for graph processing and embeddings:

```bash
pip install torch sentence-transformers requests pytest torch-geometric --break-system-packages
```

### 2. Run the Extraction Demo
Execute the full pipeline (Concept Embedding → GNN Refinement → V-Predicate Assembly) to verify the extraction of real-world concepts:

```bash
python3 -m a_quantale_theoretic_approach.demo_pipeline
```

The output will display the generated **Product Quantales** for concepts like Art, Dice, and Fire:

```lisp
(= (VPredicate Art beautiful)      (ProductQuantale (Axiom_Default_Structural) 0.103))
(= (VPredicate Dice numbered)     (ProductQuantale (Axiom_Default_Structural) 0.239))
```

### 3. Verify Logical Consistency
Run the algebraic test suite to ensure that all extracted truth values adhere to Quantale axioms (residuation, commutativity, and ordering):

```bash
python3 -m pytest a_quantale_theoretic_approach/tests/test_truth_value_pipeline.py -v
```

---

## Technical Pipeline (Phase 1)

### 1. Semantic Grounding (`extractor/concept_extractor.py`)
- **Purpose**: Maps concepts and properties to a high-dimensional vector space.
- **Implementation**: Uses `all-mpnet-base-v2` (768-dim) sentence transformers to ensure context-aware property embeddings.

### 2. Truth-Value Refinement (`extractor/gnn_truth_value.py`)
- **Purpose**: Refines the statistical "strength" of properties using structural relations.
- **Implementation**: A 2-layer **Graph Attention Network (GAT)** trained on the **CSLB Concept Property Norms** and **ConceptNet** (AtomSpace) data.

### 3. Mathematical Alignment (`core_representation/`)
- **LogicQuantale**: Encodes the symbolic relation skeleton (e.g., *IsA*, *Partof*) into algebraic axioms.
- **TruthValueQuantale**: Ensures all numeric outputs satisfy the mathematical properties of a commutative residented quantale.

---

## (Optional) Training and Customization

### Re-Training the Model
To re-train the underlying GNN on specific subsections of the OpenCog AtomSpace dataset:

```bash
python3 -m a_quantale_theoretic_approach.extractor.gnn_trainer --data_dir path/to/concept-atomspace --batch_size 200
```

### Configuration
Pre-trained weights are stored in `a_quantale_theoretic_approach/extractor/gnn_weights.pth` and are loaded automatically by the `demo_pipeline.py`.
