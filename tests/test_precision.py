import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,precision,expected", [
    ("10/3", None, pytest.approx(3.333333333, rel=1e-9)),
    ("10/3", 2, 3.33),
    ("pi", 4, 3.1416),
    ("sqrt(2)", 3, 1.414),
])
def test_precision(expr, precision, expected):
    assert calculator(expr, precision=precision) == expected
