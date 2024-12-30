def gcd(num1: int, num2: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    The algorithm assumes the GCD remains the same when the larger number is replaced with the 
    remainder of its division by the smaller number.

    a = bq + r
    r = a - bq
    If a and b share the same GCD, the remainder r will also share the same GCD.
    """
    # Convert numbers with a decimal of zero to integers or changing negative to positive
    if num1 == int(num1):
        num1 = abs(int(num1))
    if num2 == int(num2):
        num2 = abs(int(num2))

    # Ensure the inputs are integers
    if not isinstance(num1, int):
        raise ValueError(f"{num1} is not an integer")
    if not isinstance(num2, int):
        raise ValueError(f"{num2} is not an integer")
    
    # Swap numbers to ensure the first is greater for easier iteration
    if num1 < num2:
        num1, num2 = num2, num1
    
    # Iteratively compute the GCD
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1
