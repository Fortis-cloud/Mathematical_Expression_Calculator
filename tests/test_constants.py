import pytest
from calculator import calculator
import math

@pytest.mark.parametrize("expr,expected", [
    ("pi", pytest.approx(math.pi, rel=1e-9)),
    ("2*pi", pytest.approx(2*math.pi, rel=1e-9)),
    ("e", pytest.approx(math.e, rel=1e-9)),
    ("e**2", pytest.approx(math.e**2, rel=1e-9)),
    ("tau", pytest.approx(math.tau, rel=1e-9)),
    ("tau/2", pytest.approx(math.pi, rel=1e-9)),
    ("inf + 1", float('inf')),
    ("1/inf", 0.0),
])
def test_constants(expr, expected):
    assert calculator(expr) == expected
