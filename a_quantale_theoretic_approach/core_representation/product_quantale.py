from .quantale_base import QuantaleValue
from .logic_quantale import LogicQuantale
from .truth_value_quantale import TruthValueQuantale

class ProductQuantale(QuantaleValue):
    """
    Implementation of Q = Q_logic × Q_tv.
    Fuses structural possible-worlds with fuzzy truth values.
    """
    def __init__(self, logic_val: LogicQuantale, tv_val: TruthValueQuantale):
        self.logic = logic_val
        self.tv = tv_val
        # The 'value' is a tuple of the underlying sets and floats
        super().__init__((self.logic.value, self.tv.value))

    def tensor(self, other: 'ProductQuantale') -> 'ProductQuantale':
        # Component-wise conjunction (⊗)
        return ProductQuantale(self.logic * other.logic, self.tv * other.tv)

    def join(self, other: 'ProductQuantale') -> 'ProductQuantale':
        # Component-wise disjunction (⊕)
        return ProductQuantale(self.logic + other.logic, self.tv + other.tv)

    def residuation(self, other: 'ProductQuantale') -> 'ProductQuantale':
        # Component-wise implication (⇒)
        return ProductQuantale(self.logic >> other.logic, self.tv >> other.tv)

    def less_eq(self, other: 'ProductQuantale') -> bool:
        # Partial order holds ONLY if it holds for both components
        return (self.logic <= other.logic) and (self.tv <= other.tv)

    def to_metta(self) -> str:
        """Serializes the Python object into a PeTTa-compatible string."""
        logic_str = " ".join(self.logic.value) if self.logic.value else "EmptyLogic"
        return f"(ProductQuantale ({logic_str}) {self.tv.value})"