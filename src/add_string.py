from src.modeled_errors import InvalidInputError, NegativeNumberError


def add_string(numbers_str):
    """
    Add a string of numbers separated by delimiters and return the sum.
    
    Supports custom delimiters specified at the beginning of the string:
    "//[delimiter]\n[numbers...]" format.
    
    Args:
        numbers_str (str): A string of numbers separated by delimiters
        
    Returns:
        int: The sum of the numbers
        
    Raises:
        InvalidInputError: If the input contains non-numeric values or empty strings between delimiters
        NegativeNumberError: If the input contains negative numbers
    """
    
    if not numbers_str.strip():
        return 0
    
    # Check if custom delimiter is specified
    if numbers_str.startswith("//"):
        # Find the end of the delimiter line
        delimiter_end = numbers_str.find('\n')
        if delimiter_end == -1:
            raise InvalidInputError("Invalid custom delimiter format: missing newline")
        
        # Extract the delimiter (remove "//" prefix)
        delimiter = numbers_str[2:delimiter_end]
        if not delimiter:
            raise InvalidInputError("Invalid custom delimiter: delimiter cannot be empty")
        
        # Extract the numbers part (after the newline)
        numbers_part = numbers_str[delimiter_end + 1:]
    else:
        # Use comma and newline as default delimiters
        delimiter = ','
        numbers_part = numbers_str
    
    if not numbers_part:
        return 0
    
    try:
        # Process the numbers part
        numbers = []
        negative_numbers = []
        
        for line in numbers_part.split('\n'):
            for num in line.split(delimiter):
                stripped_num = num.strip()
                if stripped_num:  # Only add non-empty strings
                    int_num = int(stripped_num)
                    if int_num < 0:
                        negative_numbers.append(str(int_num))
                    else:
                        numbers.append(int_num)
                # else:
                #     # Empty string between delimiters is invalid
                #     raise InvalidInputError("Invalid input:" + numbers_str)
        
        # Check for negative numbers and raise exception if found
        if negative_numbers:
            error_message = "negative numbers not allowed " + ", ".join(negative_numbers)
            raise NegativeNumberError(error_message)
            
    except ValueError:
        raise InvalidInputError("Invalid input:" + numbers_str)
    
    return sum(numbers)
