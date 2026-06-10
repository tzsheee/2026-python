def digit_root(n: int) -> int:
    """Return the digital root of n.

    Repeatedly sum the digits of n until a single-digit number remains.
    Raises ValueError if n < 1.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if n < 1:
        raise ValueError("n must be >= 1")
    # Use the congruence formula for digital root for efficiency
    if n < 10:
        return n
    return 1 + (n - 1) % 9
