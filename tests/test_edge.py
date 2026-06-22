import pytest
from calculator import calculator, TokenizeError, ParseError, EvaluationError

def test_empty_expression():
    with pytest.raises(ValueError, match="empty expression"):
        calculator("")
    with pytest.raises(ValueError, match="empty expression"):
        calculator(" ")

def test_invalid_char():
    with pytest.raises(TokenizeError, match="unexpected character"):
        calculator("2 @ 3")

def test_parse_errors():
    with pytest.raises(ParseError):
        calculator("2 +")
    with pytest.raises(ParseError):
        calculator("* 2")
    with pytest.raises(ParseError):
        calculator("(2+3")
    with pytest.raises(ParseError):
        calculator("(2+3))")
    with pytest.raises(ParseError):
        calculator("sqrt()")
    with pytest.raises(ParseError):
        calculator("sqrt(1, 2)")
    with pytest.raises(ParseError):
        calculator("min()")

def test_evaluation_errors():
    with pytest.raises(EvaluationError, match="unknown variable 'z'"):
        calculator("z + 1")
    with pytest.raises(EvaluationError, match="unknown function 'foo'"):
        calculator("foo(1)")
    with pytest.raises(EvaluationError, match="sqrt of negative"):
        calculator("sqrt(-1)")
    with pytest.raises(EvaluationError, match="log of non-positive"):
        calculator("log(0)")
    with pytest.raises(EvaluationError, match="factorial requires non-negative integer"):
        calculator("factorial(-1)")
    with pytest.raises(EvaluationError, match="factorial requires non-negative integer"):
        calculator("factorial(3.5)")

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator("10/0")
    with pytest.raises(ZeroDivisionError):
        calculator("10//0")
    with pytest.raises(ZeroDivisionError):
        calculator("10%0")
