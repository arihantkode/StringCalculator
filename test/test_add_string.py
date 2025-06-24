import pytest
from src.add_string import add_string
from src.invalid_input_error import InvalidInputError


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
        assert add_string("-5") == -5
    
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

    def test_negative_numbers(self):
        """Test that negative numbers are handled correctly."""
        assert add_string("-1,-2,-3") == -6
        assert add_string("-1,-2,-3,-4,-5") == -15
        assert add_string("-10,-20,-30") == -60
    
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

    def test_newlines_negative_numbers(self):
        """Test newlines with negative numbers."""
        assert add_string("-1\n-2\n-3") == -6
        assert add_string("1\n-1\n0") == 0

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