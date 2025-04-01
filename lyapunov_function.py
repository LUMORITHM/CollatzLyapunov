import math
from modular_penalty import alpha

def V(n: int, streak: int, beta: float = 0.7) -> float:
    """
    Computes the Lyapunov-like function V(n) = log2(n) + alpha(n mod 16) + beta * streak.

    Parameters:
        n (int): Current value in the Collatz trajectory.
        streak (int): The current growth streak counter. Must be a non-negative integer.
        beta (float): Weight applied to the growth streak. Default is 0.7.

    Returns:
        float: The Lyapunov-like value V(n).

    Raises:
        ValueError: If n is not a positive integer or if streak is negative.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if streak < 0:
        raise ValueError("streak must be a non-negative integer.")

    return math.log2(n) + alpha(n % 16) + beta * streak
