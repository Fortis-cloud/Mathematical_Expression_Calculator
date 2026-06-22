import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("1e3", 1000),
    ("1.5e-2", 0.015),
    ("2E+4", 20000),
    ("1e3 + 1", 1001),
    ("1_000 + 2_000", 3000),
    ("1_000_000 * 2", 2000000),
])
def test_scientific_and_underscore(expr, expected):
    assert calculator(expr) == expected
