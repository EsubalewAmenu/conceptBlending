from .product_quantale import ProductQuantale

class VPredicateConcept:
    """
    Represents a concept where every property is a V-Predicate 
    (mapping to a Product Quantale).
    """
    def __init__(self, concept_name: str):
        self.name = concept_name
        self.properties: dict[str, ProductQuantale] = {}

    def add_property(self, property_name: str, quantale: ProductQuantale):
        self.properties[property_name] = quantale

    def to_metta_assertions(self) -> list[str]:
        """Generates the MeTTa assertions to load this concept into PeTTa."""
        assertions = []
        for prop, quantale in self.properties.items():
            assertions.append(
                f"(= (VPredicate {self.name} {prop}) {quantale.to_metta()})"
            )
        return assertions