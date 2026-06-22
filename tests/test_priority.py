import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("2+3*4", 14),
    ("(2+3)*4", 20),
    ("10-2*3", 4),
    ("100/10/2", 5.0),
    ("10-20+5", -5),
    ("2*3+4*5", 26),
])
def test_priority(expr, expected):
    assert calculator(expr) == expected
