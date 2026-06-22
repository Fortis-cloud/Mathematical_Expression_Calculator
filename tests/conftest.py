import pytest
from calculator import calculator, Calculator


@pytest.fixture
def calc():
    return Calculator()

@pytest.fixture
def eval_func():
    return calculator
