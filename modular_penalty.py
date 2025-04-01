def alpha(n_mod_16: int) -> float:
    """
    Returns the modular penalty α(n mod 16) as defined in the paper.

    The penalty values are predetermined based on the residue of n modulo 16.

    Parameters:
        n_mod_16 (int): The residue of n modulo 16. Must be in the range [0, 15].

    Returns:
        float: Penalty value associated with the residue.

    Raises:
        ValueError: If n_mod_16 is not an integer between 0 and 15 (inclusive).
    """
    penalties = {
        0: -0.06,  1: -0.05,  2: -0.04,  3:  0.10,
        4: -0.03,  5:  0.06,  6: -0.04,  7:  0.08,
        8: -0.02,  9: -0.04, 10: -0.05, 11:  0.11,
       12: -0.06, 13: -0.05, 14: -0.03, 15:  0.09
    }

    try:
        return penalties[n_mod_16]
    except KeyError:
        raise ValueError("Input must be an integer between 0 and 15 (inclusive).")
