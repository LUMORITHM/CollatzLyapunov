from delta_v_analysis import compute_delta_V_trajectory
from typing import Dict
from collections import OrderedDict

def analyze_trajectory(n0: int, beta: float = 0.7, max_steps: int = 1000) -> Dict[str, float]:
    """
    Analyzes the ΔV behavior of a Collatz trajectory starting from n0.

    Parameters:
        n0 (int): Initial seed. Must be a positive integer.
        beta (float): Weighting factor for the growth streak. Default is 0.7.
        max_steps (int): Maximum steps to simulate. Default is 1000.

    Returns:
        Dict[str, float]: Dictionary containing average ΔV, positive step rate, min/max ΔV.

    Raises:
        ValueError: If n0 is not a positive integer.
    """
    if n0 <= 0:
        raise ValueError("Initial seed n0 must be a positive integer.")

    delta_vs = compute_delta_V_trajectory(n0, beta, max_steps)

    if not delta_vs:
        return OrderedDict([
            ("n0", n0),
            ("avg_delta_V", 0.0),
            ("pos_rate", 0.0),
            ("max_delta_V", 0.0),
            ("min_delta_V", 0.0)
        ])

    total = sum(delta_vs)
    count = len(delta_vs)
    pos_count = sum(1 for dv in delta_vs if dv > 0)

    return OrderedDict([
        ("n0", n0),
        ("avg_delta_V", total / count),
        ("pos_rate", pos_count / count),
        ("max_delta_V", max(delta_vs)),
        ("min_delta_V", min(delta_vs))
    ])
