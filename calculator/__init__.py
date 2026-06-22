from .core import evaluate
from .exceptions import CalculatorError, TokenizeError, ParseError, EvaluationError

class Calculator:
    def __init__(
        self,
        variables: dict[str, float | int] | None = None,
        precision: int | None = None,
        angle_mode: str = "rad",
    ) -> None:
        self.variables = variables or {}
        self.precision = precision
        self.angle_mode = angle_mode

    def evaluate(self, expression: str, verbose: bool = False) -> float | int:
        return evaluate(expression, self.variables, self.precision, self.angle_mode, verbose)


def calculator(
    expression: str,
    *,
    verbose: bool = False,
    variables: dict[str, float | int] | None = None,
    precision: int | None = None,
    angle_mode: str = "rad",
) -> float | int:
    return evaluate(expression, variables or {}, precision, angle_mode, verbose)


__all__ = [
    "calculator",
    "Calculator",
    "CalculatorError",
    "TokenizeError",
    "ParseError",
    "EvaluationError",
]
