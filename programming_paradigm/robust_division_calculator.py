# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Perform a safe division with robust error handling.

    Returns:
        str: Success message with the result, or an error message.
    """
    # Handle non-numeric inputs
    try:
        num = float(numerator)
        den = float(denominator)
    except (ValueError, TypeError):
        return "Error: Please enter numeric values only."

    # Handle division by zero
    try:
        result = num / den
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    return f"The result of the division is {result}"
