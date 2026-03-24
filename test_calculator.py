"""Unit tests for the calculator module."""

from calculator import add, subtract


def test_add_positive_numbers():
    """Test addition with positive numbers."""
    assert add(2, 3) == 5


def test_add_negative_numbers():
    """Test addition with negative numbers."""
    assert add(-2, -3) == -5


def test_subtract():
    """Test subtraction."""
    assert subtract(10, 4) == 6

def test_add_positive_numbers():
    assert add(2, 3) == 99   # wrong expected value