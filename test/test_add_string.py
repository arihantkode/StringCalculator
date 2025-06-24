import pytest
from src.add_string import add_string
from src.modeled_errors import InvalidInputError, NegativeNumberError


class TestAddString:
    """Test cases for the add_string function."""
    
    def test_empty_string(self):
        """Test that empty string returns 0."""
        assert add_string("") == 0
    
    def test_single_number(self):
        """Test that single number returns the number itself."""
        assert add_string("1") == 1
        assert add_string("42") == 42
        assert add_string("0") == 0
    
    def test_two_numbers(self):
        """Test that two comma-separated numbers return their sum."""
        assert add_string("1,5") == 6
        assert add_string("10,20") == 30
        assert add_string("0,0") == 0
    
    def test_multiple_numbers(self):
        """Test that multiple comma-separated numbers return their sum."""
        assert add_string("1,2,3,4,5") == 15
        assert add_string("10,20,30") == 60
        assert add_string("1,1,1,1,1,1") == 6
        assert add_string("0,0,0,0") == 0
    
    def test_large_numbers(self):
        """Test that large numbers are handled correctly."""
        assert add_string("1000,2000") == 3000
        assert add_string("999999,1") == 1000000
        assert add_string("1000000,2000000,3000000") == 6000000
    
    def test_zero_values(self):
        """Test that zero values are handled correctly."""
        assert add_string("0,0,0") == 0
        assert add_string("1,0,1") == 2
        assert add_string("0,5,0") == 5
    
    def test_single_zero(self):
        """Test that single zero returns zero."""
        assert add_string("0") == 0

    def test_whitespace_handling(self):
        """Test various whitespace scenarios."""
        assert add_string(" 1 ") == 1
        assert add_string(" 1 , 2 , 3 ") == 6
        assert add_string("\t1,\n2,\r3") == 6
        assert add_string("   1   ,   2   ,   3   ") == 6

    def test_negative_numbers_single(self):
        """Test that single negative number raises exception."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1"):
            add_string("-1")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -5"):
            add_string("-5")

    def test_negative_numbers_multiple(self):
        """Test that multiple negative numbers raise exception with all numbers listed."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -2, -3"):
            add_string("-1,-2,-3")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -10, -20, -30"):
            add_string("-10,-20,-30")

    def test_negative_numbers_mixed(self):
        """Test that mixed positive and negative numbers raise exception with only negative numbers listed."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -3"):
            add_string("1,-1,2,-3,4")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -5"):
            add_string("1,2,3,-5,4,5")

    def test_negative_numbers_with_newlines(self):
        """Test that negative numbers with newlines raise exception."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -2"):
            add_string("1\n-1\n-2\n3")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -3"):
            add_string("1,-1\n2,-3\n4")

    def test_negative_numbers_with_custom_delimiter(self):
        """Test that negative numbers with custom delimiters raise exception."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -2"):
            add_string("//;\n1;-1;-2;3")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -5"):
            add_string("//|\n1|2|3|-5|4|5")

    def test_negative_numbers_complex(self):
        """Test complex scenarios with negative numbers."""
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -1, -2, -3, -4, -5"):
            add_string("-1,-2,-3,-4,-5")
        
        with pytest.raises(NegativeNumberError, match="negative numbers not allowed -999999"):
            add_string("999999,-999999,1")

    def test_invalid_inputs(self):
        """Test that invalid inputs raise appropriate exceptions."""
        with pytest.raises(InvalidInputError):
            add_string("1,a,3")
        with pytest.raises(InvalidInputError):
            add_string("one, one, one")

    def test_invalid_inputs_with_spaces(self):
        """Test that invalid inputs with spaces raise appropriate exceptions."""
        with pytest.raises(InvalidInputError):
            add_string("1, a, 3")
        with pytest.raises(InvalidInputError):
            add_string("one, one, one")
        # with pytest.raises(InvalidInputError):
        #     add_string("1,2,  ,  3,4, ,5")
               
    def test_invalid_inputs_with_newlines(self):
        """Test that invalid inputs with newlines raise appropriate exceptions."""
        with pytest.raises(InvalidInputError):
            add_string("1,\na, 3")
    
    def test_valid_inputs_with_newlines(self):
        """Test that valid inputs with newlines are handled correctly."""
        assert add_string("1\n2,3") == 6

    def test_newlines_as_delimiters(self):
        """Test that newlines can be used as delimiters."""
        assert add_string("1\n2\n3") == 6
        assert add_string("1\n2,3") == 6
        assert add_string("1,2\n3") == 6
        assert add_string("1\n2\n3,4,5") == 15

    def test_mixed_delimiters_complex(self):
        """Test complex combinations of newlines and commas."""
        assert add_string("1\n2,3\n4,5,6") == 21
        assert add_string("1,2\n3,4\n5") == 15
        assert add_string("1\n2\n3\n4\n5") == 15

    def test_newlines_with_spaces(self):
        """Test newlines with spaces around numbers."""
        assert add_string(" 1 \n 2 \n 3 ") == 6
        assert add_string("1 , 2\n3 , 4") == 10

    def test_newlines_large_numbers(self):
        """Test newlines with large numbers."""
        assert add_string("1000\n2000\n3000") == 6000
        assert add_string("999999\n1") == 1000000

    def test_newlines_single_number(self):
        """Test newlines with single number."""
        assert add_string("42\n") == 42
        assert add_string("\n42") == 42
        assert add_string("42\n\n") == 42

    def test_newlines_empty_lines(self):
        """Test newlines with empty lines."""
        assert add_string("1\n\n2\n\n3") == 6
        assert add_string("\n1\n2\n3\n") == 6

    def test_newlines_invalid_numbers(self):
        """Test newlines with invalid numbers."""
        with pytest.raises(InvalidInputError):
            add_string("1\na\n3")
        
        with pytest.raises(InvalidInputError):
            add_string("1,2\nabc\n4,5")

    def test_custom_delimiter_semicolon(self):
        """Test custom delimiter with semicolon."""
        assert add_string("//;\n1;2") == 3
        assert add_string("//;\n1;2;3;4;5") == 15
        assert add_string("//;\n10;20;30") == 60

    def test_custom_delimiter_pipe(self):
        """Test custom delimiter with pipe character."""
        assert add_string("//|\n1|2|3") == 6
        assert add_string("//|\n10|20|30|40") == 100

    def test_custom_delimiter_asterisk(self):
        """Test custom delimiter with asterisk."""
        assert add_string("//*\n1*2*3*4") == 10
        assert add_string("//*\n5*10*15") == 30

    def test_custom_delimiter_with_spaces(self):
        """Test custom delimiter with spaces around numbers."""
        assert add_string("//;\n1 ; 2 ; 3") == 6
        assert add_string("//|\n 1 | 2 | 3 ") == 6

    def test_custom_delimiter_large_numbers(self):
        """Test custom delimiter with large numbers."""
        assert add_string("//;\n1000;2000;3000") == 6000
        assert add_string("//|\n999999|1") == 1000000

    def test_custom_delimiter_single_number(self):
        """Test custom delimiter with single number."""
        assert add_string("//;\n42") == 42
        assert add_string("//|\n0") == 0

    def test_custom_delimiter_empty_numbers(self):
        """Test custom delimiter with empty numbers part."""
        assert add_string("//;\n") == 0

    def test_invalid_custom_delimiter_format(self):
        """Test invalid custom delimiter format."""
        with pytest.raises(InvalidInputError):
            add_string("//;1;2")  # Missing newline
        
        with pytest.raises(InvalidInputError):
            add_string("//\n1,2")  # Empty delimiter

    def test_custom_delimiter_invalid_numbers(self):
        """Test custom delimiter with invalid numbers."""
        with pytest.raises(InvalidInputError):
            add_string("//;\n1;a;3")
        
        with pytest.raises(InvalidInputError):
            add_string("//|\n1|2|abc|4")

    def test_mixed_delimiters(self):
        """Test that custom delimiter doesn't interfere with comma delimiter."""
        # Custom delimiter should be used
        assert add_string("//;\n1;2;3") == 6
        
        # Comma delimiter should still work for non-custom format
        assert add_string("1,2,3") == 6

    def test_custom_delimiter_with_whitespace_in_delimiter(self):
        """Test custom delimiter with whitespace in delimiter definition."""
        with pytest.raises(InvalidInputError):
            add_string("// ; \n1;2;3")  # Whitespace in delimiter

    def test_custom_delimiter_multiple_characters(self):
        """Test custom delimiter with multiple characters."""
        assert add_string("//**\n1**2**3") == 6
        assert add_string("//--\n10--20--30") == 60

    def test_custom_delimiter_with_newlines(self):
        """Test custom delimiter with newlines in numbers."""
        assert add_string("//;\n1;2\n3;4") == 10
        assert add_string("//|\n1|2\n3|4\n5") == 15