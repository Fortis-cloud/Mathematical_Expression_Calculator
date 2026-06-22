import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("0.1 + 0.2", pytest.approx(0.3, rel=1e-9)),
    ("1/3 + 1/3 + 1/3", pytest.approx(1.0, rel=1e-9)),
    ("sqrt(2) * sqrt(2)", pytest.approx(2.0, rel=1e-9)),
    ("sin(pi)", pytest.approx(0.0, abs=1e-10)),
    ("cos(pi/2)", pytest.approx(0.0, abs=1e-10)),
])
def test_float_precision(expr, expected):
    assert calculator(expr) == expected
