from src.invalid_input_error import InvalidInputError


def add_string(numbers_str):
    """
    Add a string of comma-separated numbers and return the sum.
    
    Args:
        numbers_str (str): A string of comma-separated numbers
        
    Returns:
        int: The sum of the numbers
        
    Raises:
        InvalidInputError: If the input contains non-numeric values
    """
    
    if not numbers_str:
        return 0
    
    try:
        # Split the string by comma and convert each part to integer
        numbers = [int(num.strip()) for num in numbers_str.split(',')]
    except ValueError:
        raise InvalidInputError("Invalid input: " + numbers_str)
    
    return sum(numbers)
