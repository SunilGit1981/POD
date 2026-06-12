def factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    The factorial of a non-negative integer n, denoted by n!, is the product
    of all positive integers less than or equal to n.

    Special cases:
    - The factorial of 0 (0!) is defined as 1.
    - The factorial of 1 (1!) is 1.

    Args:
        n: An integer for which to calculate the factorial.

    Returns:
        The factorial of n.

    Raises:
        ValueError: If n is a negative number.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result