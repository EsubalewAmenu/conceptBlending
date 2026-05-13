from .quantale_base import QuantaleValue

class LogicQuantale(QuantaleValue[set]):
    """
    Implementation of Q_logic: (P(W), ∩, ∪, W, ⊆)
    Handles the strict relational and topology-preserving structural information.
    """
    def __init__(self, value: set, universal_set: set = None):
        super().__init__(set(value))
        # W represents the total possible worlds/axioms
        self.universal_set = universal_set if universal_set is not None else set()

    def tensor(self, other: 'LogicQuantale') -> 'LogicQuantale':
        # ⊗ is set intersection (∩)
        return LogicQuantale(self.value.intersection(other.value), self.universal_set)

    def join(self, other: 'LogicQuantale') -> 'LogicQuantale':
        # ⊕ is set union (∪)
        return LogicQuantale(self.value.union(other.value), self.universal_set)

    def residuation(self, other: 'LogicQuantale') -> 'LogicQuantale':
        # ⇒ directly implements: B ∪ ~A
        # ~A is the complement of A relative to the universal set W
        not_a = self.universal_set.difference(self.value)
        return LogicQuantale(other.value.union(not_a), self.universal_set)

    def less_eq(self, other: 'LogicQuantale') -> bool:
        # ≤ is subset relation (⊆)
        return self.value.issubset(other.value)