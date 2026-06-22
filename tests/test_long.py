import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("1+2+3+4+5+6+7+8+9+10", 55),
    ("1*2*3*4*5*6*7*8*9*10", 3628800),
    ("1+2+3+4+5*6*7*8*9*10*12*0+2/2+3", 5),
    ("sqrt(3**2 + 4**2)", 5.0),
    ("log(e**2)", pytest.approx(2.0, rel=1e-9)),
    ("factorial(5) + factorial(3)", 126),
    ("max(1,2,3) * min(4,5,6) + sqrt(16)", 22),
    ("sin(pi/2) + cos(0) + tan(0)", pytest.approx(2.0, rel=1e-9)),
])
def test_long_expressions(expr, expected):
    assert calculator(expr) == expected
