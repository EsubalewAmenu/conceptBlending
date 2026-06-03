from typing import Tuple

def calculate_jaccard_strength(count_u: int, count_v: int, count_uv: int) -> float:
    """
    Implements Equation (38) - M_P^{freq}(u, v) from the framework.
    Calculates the Jaccard index based on provided individual and joint frequencies.
    """
    # Safety guardrail: if either property has never been seen, habit strength is 0
    if count_u == 0 or count_v == 0:
        return 0.0
        
    # Denominator logic: count(u) + count(v) - count(u, v)
    denominator = count_u + count_v - count_uv
    
    # Safety guardrail to avoid ZeroDivisionError
    if denominator == 0:
        return 0.0
        
    return count_uv / denominator