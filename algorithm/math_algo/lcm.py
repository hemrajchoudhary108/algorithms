from algorithm.math_algo import gcd

def lcm(num1: int, num2: int) -> int:
    """
    Calculates the least common multiple (LCM) of two numbers.
    The LCM is the smallest positive integer that is divisible by both numbers.
    """
    # Check if the inputs are integers or floats equivalent to integers
    if isinstance(num1, float) and num1.is_integer():
        num1 = int(num1)
    elif not isinstance(num1, int):
        raise ValueError(f"{num1} is not an integer or an integer-equivalent float")

    if isinstance(num2, float) and num2.is_integer():
        num2 = int(num2)
    elif not isinstance(num2, int):
        raise ValueError(f"{num2} is not an integer or an integer-equivalent float")

    # Calculate GCD of the two numbers
    gcd_of_two = gcd(num1, num2)

    # Handle the case where GCD is 0
    if gcd_of_two == 0:
        return 0

    # Calculate and return the LCM
    return abs(num1 * num2) // gcd_of_two
