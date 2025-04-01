import math
from collatz_map import collatz_step
from growth_streak import update_growth_streak
from modular_penalty import alpha
from typing import List, Tuple

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

def generate_descent_trajectory(n0: int, beta: float = 0.7, steps: int = 64) -> List[Tuple[int, int, float]]:
    """
    Simulates a trajectory and returns a list of (n_i, streak_i, ΔV_i)

    Parameters:
        n0 (int): Starting value. Must be a positive integer.
        beta (float): Weight for the growth streak. Default is 0.7.
        steps (int): Number of steps to simulate. Default is 64.

    Returns:
        List[Tuple[int, int, float]]: List of (n, streak, ΔV) tuples.

    Raises:
        ValueError: If n0 is not a positive integer or if steps is not a positive integer.
    """
    if n0 <= 0:
        raise ValueError("n0 must be a positive integer.")
    if steps <= 0:
        raise ValueError("steps must be a positive integer.")

    trajectory = []
    n = n0
    streak = 0

    for _ in range(steps):
        V_n = V(n, streak, beta)
        next_n = collatz_step(n)
        next_streak = update_growth_streak(n, streak)
        V_next = V(next_n, next_streak, beta)

        delta_V = V_next - V_n
        trajectory.append((n, streak, delta_V))

        n = next_n
        streak = next_streak

        if n == 1:
            break

    return trajectory

def print_trajectory_as_sat_comments(trajectory: List[Tuple[int, int, float]]):
    """
    Prints each step with ΔV < 0 encoded as a comment line (to later turn into SAT clauses)

    Parameters:
        trajectory (List[Tuple[int, int, float]]): Output of generate_descent_trajectory
    """
    print("c SAT Encoding of Descent Constraints (as comments)")
    for i, (n, streak, delta_V) in enumerate(trajectory):
        print(f"c Step {i}: n = {n}, streak = {streak}, ΔV = {delta_V:.6f} {'[FAIL]' if delta_V > 0 else ''}")

# Example usage
if __name__ == "__main__":
    n0 = 27
    trajectory = generate_descent_trajectory(n0, beta=0.7, steps=64)
    print_trajectory_as_sat_comments(trajectory)
