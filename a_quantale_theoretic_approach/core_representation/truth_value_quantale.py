from .quantale_base import QuantaleValue

class TruthValueQuantale(QuantaleValue[float]):
    """
    Implementation of Q_tv: ([0,1], ×, +, 1, ≤)
    Handles the fuzzy, graded property values extracted by the LLM.
    """
    def __init__(self, value: float):
        # Ensure the value is strictly bounded between 0.0 and 1.0
        super().__init__(max(0.0, min(float(value), 1.0)))

    def tensor(self, other: 'TruthValueQuantale') -> 'TruthValueQuantale':
        # ⊗ is standard multiplication for product logic
        return TruthValueQuantale(self.value * other.value)

    def join(self, other: 'TruthValueQuantale') -> 'TruthValueQuantale':
        # ⊕ is bounded addition (supremum in this context)
        return TruthValueQuantale(min(self.value + other.value, 1.0))

    def residuation(self, other: 'TruthValueQuantale') -> 'TruthValueQuantale':
        a = self.value
        b = other.value
        if a == 0.0:
            return TruthValueQuantale(1.0)
        return TruthValueQuantale(min(b / a, 1.0))

    def less_eq(self, other: 'TruthValueQuantale') -> bool:
        # ≤ is standard numeric less-than-or-equal
        return self.value <= other.value