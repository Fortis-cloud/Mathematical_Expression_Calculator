import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,expected", [
    ("2+3", 5),
    ("10-4", 6),
    ("6*7", 42),
    ("15/3", 5),
    ("15/4", 3.75),
    ("17%5", 2),
    ("17//5", 3),
    ("50%", 0.5),
    ("200*10%", 20.0),
    ("(100+50)%", 1.5),
])
def test_basic_operations(expr, expected):
    assert calculator(expr) == expected
