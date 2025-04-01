import math
from typing import List

def collatz_step(n: int) -> int:
    """
    Applies the single-step Collatz transformation:
        - If n is even: return n // 2
        - If n is odd:  return (3 * n + 1) // 2

    Parameters:
        n (int): Current value in the trajectory

    Returns:
        int: Next value in the Collatz trajectory
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer")

    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n + 1) // 2

def full_trajectory(n0: int, max_steps: int = 1000) -> List[int]:
    """
    Generates the Collatz trajectory starting from n0.

    Parameters:
        n0 (int): Initial seed
        max_steps (int): Maximum number of iterations to prevent infinite loops

    Returns:
        List[int]: List of integers representing the trajectory
    """
    if n0 <= 0:
        raise ValueError("Initial seed must be a positive integer")

    trajectory = [n0]
    n = n0

    for _ in range(max_steps):
        if n == 1:
            break
        n = collatz_step(n)
        trajectory.append(n)

    return trajectory
