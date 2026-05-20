from collections import defaultdict
from typing import Tuple, Dict, Set
from jaccard_co_occurrence import calculate_jaccard_strength

class HabitMemory:
    """
    KR 1 & KR 2: Handles long-term Peircean habit memory representation,
    storage, retrieval, and reinforcement operations.
    """
    def __init__(self):
        # KR 1 / Section 9.1: Data structures for storing historical counts
        self.property_counts: Dict[str, int] = defaultdict(int)         # count(u)
        self.pair_counts: Dict[Tuple[str, str], int] = defaultdict(int) # count(u, v)
        self.total_blends_processed = 0

    def _get_ordered_pair(self, u: str, v: str) -> Tuple[str, str]:
        """Ensures commutative property pairs map to the same key symmetrically."""
        return (u, v) if u < v else (v, u)

    def register_successful_blend(self, blend_properties: Set[str]):
        """
        KR 2 & KR 4: Habit Formation / Reinforcement loop.
        Registers properties from selected or non-dominated blends into memory.
        """
        self.total_blends_processed += 1
        prop_list = list(blend_properties)
        
        # 1. Update individual property counts
        for prop in prop_list:
            self.property_counts[prop] += 1
            
        # 2. Update joint pairwise counts
        for i in range(len(prop_list)):
            for j in range(i + 1, len(prop_list)):
                pair = self._get_ordered_pair(prop_list[i], prop_list[j])
                self.pair_counts[pair] += 1

    def get_habit_strength(self, u: str, v: str) -> float:
        """Retrieves frequencies from memory structures and sends them to the math engine."""
        count_u = self.property_counts.get(u, 0)
        count_v = self.property_counts.get(v, 0)
        
        pair = self._get_ordered_pair(u, v)
        count_uv = self.pair_counts.get(pair, 0)
        
        # Route processing to our math module
        return calculate_jaccard_strength(count_u, count_v, count_uv)

    def calculate_blend_habit_bonus(self, candidate_properties: Set[str]) -> float:
        """KR 3 / Equation (43): Aggregates total internal habit strengths for a blend."""
        total_bonus = 0.0
        prop_list = list(candidate_properties)
        
        for i in range(len(prop_list)):
            for j in range(i + 1, len(prop_list)):
                total_bonus += self.get_habit_strength(prop_list[i], prop_list[j])
                
        return total_bonus

    def apply_habit_decay(self, gamma: float):
        """KR 2 / Section 6.4: Dynamic habit decay operation."""
        for prop in self.property_counts:
            self.property_counts[prop] = int(self.property_counts[prop] * gamma)
            
        for pair in self.pair_counts:
            self.pair_counts[pair] = int(self.pair_counts[pair] * gamma)