import pytest
from calculator import calculator

@pytest.mark.parametrize("expr,variables,expected", [
    ("x + y", {"x": 10, "y": 5}, 15),
    ("x * 2", {"x": 3.5}, 7.0),
    ("x**2 + y**2", {"x": 3, "y": 4}, 25),
    ("a*b + c", {"a": 2, "b": 3, "c": 1}, 7),
    ("x = 2; x * 3", {}, 6),
    ("a = 1; b = a + 2; a + b", {}, 4),
])
def test_variables(expr, variables, expected):
    assert calculator(expr, variables=variables) == expected
