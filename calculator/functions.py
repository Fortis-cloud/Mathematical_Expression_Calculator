import math
from typing import Callable

def _sqrt(x: float) -> float:
    if x < 0:
        raise ValueError("cannot take sqrt of negative number")
    return math.sqrt(x)

def _log(x: float) -> float:
    if x <= 0:
        raise ValueError("log of non-positive number")
    return math.log(x)

def _ln(x: float) -> float:
    return _log(x)

def _factorial(x: float) -> int:
    if not isinstance(x, int) or x < 0:
        raise ValueError("factorial requires non-negative integer")
    return math.factorial(x)

# Реестр функций
FUNCTION_MAP: dict[str, Callable[..., float | int]] = {
    "sqrt": _sqrt,
    "abs": abs,
    "pow": pow,
    "min": min,
    "max": max,
    "floor": math.floor,
    "ceil": math.ceil,
    "round": round,
    "log": _log,
    "ln": _ln,
    "log10": math.log10,
    "exp": math.exp,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "factorial": _factorial,
}
