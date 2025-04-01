
import math
from typing import List
from collatz_map import collatz_step
from modular_penalty import alpha
from growth_streak import update_growth_streak

def V(n: int, streak: int, beta: float = 0.7) -> float:
    """
    Computes the Lyapunov-like function V(n) = log2(n) + alpha(n mod 16) + beta * streak.

    Parameters:
        n (int): Current value in the Collatz trajectory.
        streak (int): The current growth streak counter. Must be a non-negative integer.
        beta (float): Weight for the growth streak. Default is 0.7.

    Returns:
        float: Value of the Lyapunov function.

    Raises:
        ValueError: If n is not a positive integer or if streak is negative.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer.")
    if streak < 0:
        raise ValueError("streak must be a non-negative integer.")
    
    return math.log2(n) + alpha(n % 16) + beta * streak

def compute_delta_V_trajectory(n0: int, beta: float = 0.7, max_steps: int = 1000) -> List[float]:
    """
    Computes ΔV for each step in the trajectory of n0 using the Lyapunov-like function.

    Parameters:
        n0 (int): Initial seed. Must be a positive integer.
        beta (float): Weight for the growth streak. Default is 0.7.
        max_steps (int): Maximum number of trajectory steps. Default is 1000.

    Returns:
        List[float]: List of ΔV values per step.

    Raises:
        ValueError: If n0 is not a positive integer.
    """
    if n0 <= 0:
        raise ValueError("Initial seed must be a positive integer.")

    n = n0
    streak = 0
    delta_Vs = []

    for _ in range(max_steps):
        if n == 1:
            break

        V_n = V(n, streak, beta)
        n_next = collatz_step(n)
        new_streak = update_growth_streak(n, streak)
        V_next = V(n_next, new_streak, beta)

        delta_Vs.append(V_next - V_n)

        n = n_next
        streak = new_streak

    return delta_Vs
