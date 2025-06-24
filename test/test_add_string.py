import pytest
from src.add_string import add_string


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