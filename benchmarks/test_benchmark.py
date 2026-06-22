import pytest
from calculator import calculator

@pytest.mark.benchmark
def test_benchmark_1000_additions(benchmark):
    expr = "+".join(["1"] * 1000) + "+1"
    result = benchmark(calculator, expr)
    assert result == 1001
