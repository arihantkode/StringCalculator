from src.invalid_input_error import InvalidInputError


def add_string(numbers_str):
    """
    Add a string of numbers separated by commas and/or newlines and return the sum.
    
    Args:
        numbers_str (str): A string of numbers separated by commas and/or newlines
        
    Returns:
        int: The sum of the numbers
        
    Raises:
        InvalidInputError: If the input contains non-numeric values
    """
    
    if not numbers_str:
        return 0
    
    try:
        # First split by newlines, then by commas
        numbers = []
        for line in numbers_str.split('\n'):
            for num in line.split(','):
                stripped_num = num.strip()
                if stripped_num:  # Only add non-empty strings
                    numbers.append(int(stripped_num))
    except ValueError:
        raise InvalidInputError("Invalid input: " + numbers_str)
    
    return sum(numbers)
