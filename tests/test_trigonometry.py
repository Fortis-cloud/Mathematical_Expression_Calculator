import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,angle_mode,expected", [
    ("sin(0)", "rad", 0.0),
    ("sin(pi/2)", "rad", pytest.approx(1.0, rel=1e-9)),
    ("sin(90)", "deg", pytest.approx(1.0, rel=1e-9)),
    ("cos(0)", "rad", 1.0),
    ("cos(60)", "deg", pytest.approx(0.5, rel=1e-9)),
    ("tan(45)", "deg", pytest.approx(1.0, rel=1e-9)),
])
def test_trigonometry(expr, angle_mode, expected):
    assert calculator(expr, angle_mode=angle_mode) == expected
