import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("sqrt(16)", 4),
    ("sqrt(2)", pytest.approx(1.414213562, rel=1e-9)),
    ("abs(-5)", 5),
    ("abs(-3.7)", 3.7),
    ("pow(2, 10)", 1024),
    ("pow(2, 0.5)", pytest.approx(1.414213562, rel=1e-9)),
    ("min(3, 1, 2)", 1),
    ("max(3, 1, 2)", 3),
    ("min(5)", 5),
    ("floor(3.7)", 3),
    ("ceil(3.2)", 4),
    ("round(3.5)", 4),
    ("log(e)", pytest.approx(1.0, rel=1e-9)),
    ("ln(e)", pytest.approx(1.0, rel=1e-9)),
    ("log10(1000)", 3.0),
    ("exp(0)", 1.0),
    ("exp(1)", pytest.approx(2.718281828, rel=1e-9)),
    ("sin(0)", 0.0),
    ("cos(0)", 1.0),
    ("factorial(0)", 1),
    ("factorial(5)", 120),
    ("factorial(10)", 3628800),
])
def test_functions(expr, expected):
    assert calculator(expr) == expected
