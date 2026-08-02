"""
Grounded Python atoms that expose McBrideOptimizer to MeTTa.
Follows the pattern used in op-constraints/op-helper-codes.py.
"""
from typing import Any
from hyperon import OperationAtom, ValueAtom
from a_quantale_theoretic_approach.optimization.macbride_derivative import (
    McBrideOptimizer, emergence_tv, uniform_valuation
)
from a_quantale_theoretic_approach.core_representation.v_predicate_parser import (
    parse_v_predicate_concept
)
from a_quantale_theoretic_approach.core_representation.v_predicate import (
    VPredicateConcept
)


def _concept_from_metta_atom(atom: Any) -> VPredicateConcept:
    """Convert a MeTTa (Concept ...) atom to a Python VPredicateConcept."""
    atom_str = str(atom)
    return parse_v_predicate_concept(atom_str)


def mcbride_py_refine(blend_atom, source_a_atom, source_b_atom, eta_atom, steps_atom):
    blend    = _concept_from_metta_atom(blend_atom)
    source_a = _concept_from_metta_atom(source_a_atom)
    source_b = _concept_from_metta_atom(source_b_atom)
    eta      = float(str(eta_atom))
    steps    = int(str(steps_atom))

    optimizer = McBrideOptimizer(
        source_a=source_a, source_b=source_b,
        eta=eta, max_steps=steps,
    )
    result = optimizer.refine(blend)
    return ValueAtom(result.refined_blend.to_metta())


def mcbride_py_emergence(blend_atom, source_a_atom, source_b_atom):
    blend    = _concept_from_metta_atom(blend_atom)
    source_a = _concept_from_metta_atom(source_a_atom)
    source_b = _concept_from_metta_atom(source_b_atom)
    score = emergence_tv(source_a, source_b, blend, uniform_valuation)
    return ValueAtom(score)


def register_mcbride_atoms(metta_instance):
    """Call this once when setting up your MeTTa runtime."""
    metta_instance.register_atom(
        "mcbride-py-refine",
        OperationAtom("mcbride-py-refine", mcbride_py_refine, unwrap=False)
    )
    metta_instance.register_atom(
        "mcbride-py-emergence",
        OperationAtom("mcbride-py-emergence", mcbride_py_emergence, unwrap=False)
    )
