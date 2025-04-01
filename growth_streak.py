def update_growth_streak(n: int, current_streak: int) -> int:
    """
    Updates the growth streak counter based on the current value of n.

    The growth streak increases if n mod 16 ∈ {3, 7, 11, 15}, else resets to 0.

    Parameters:
        n (int): Current value in the trajectory.
        current_streak (int): The current growth streak counter.

    Returns:
        int: Updated growth streak counter.
    """
    growth_prone_residues = {3, 7, 11, 15}
    if n % 16 in growth_prone_residues:
        return current_streak + 1
    else:
        return 0
