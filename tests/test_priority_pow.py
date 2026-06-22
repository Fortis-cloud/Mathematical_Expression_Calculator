import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("2**3", 8),
    ("2**3**2", 512),
    ("2**10", 1024),
    ("-2**2", -4),
    ("(-2)**2", 4),
    ("9**0.5", 3.0),
    ("0**0", 1),
    ("2**-1", 0.5),
])
def test_power_associativity(expr, expected):
    assert calculator(expr) == expected

@pytest.mark.parametrize("expr,expected", [
    ("-5+3", -2),
    ("--5", 5),
    ("- -5", 5),
    ("+5", 5),
    ("3*-2", -6),
    ("3*(-2)", -6),
    ("-(2+3)", -5),
])
def test_unary_operators(expr, expected):
    assert calculator(expr) == expected
