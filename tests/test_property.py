import pytest
from hypothesis import given, strategies as st
from calculator import calculator

@given(st.integers(min_value=-100, max_value=100),
       st.integers(min_value=-100, max_value=100))
def test_add_commutative(a, b):
    assert calculator(f"{a}+{b}") == calculator(f"{b}+{a}")

@given(st.integers(min_value=-100, max_value=100),
       st.integers(min_value=-100, max_value=100))
def test_mul_commutative(a, b):
    assert calculator(f"{a}*{b}") == calculator(f"{b}*{a}")

@given(st.integers(min_value=-100, max_value=100))
def test_add_zero(a):
    assert calculator(f"{a}+0") == a
    assert calculator(f"0+{a}") == a

@given(st.integers(min_value=-100, max_value=100))
def test_mul_one(a):
    assert calculator(f"{a}*1") == a
    assert calculator(f"1*{a}") == a

@given(st.integers(min_value=-100, max_value=100))
def test_double_negation(a):
    assert calculator(f"--{a}") == a

@given(st.integers(min_value=0, max_value=20))
def test_power_square(a):
    assert calculator(f"{a}**2") == a*a

@given(st.integers(min_value=-100, max_value=100))
def test_verbose_invariant(a):
    expr = f"{a}+{a}"
    assert calculator(expr) == calculator(expr, verbose=True)
