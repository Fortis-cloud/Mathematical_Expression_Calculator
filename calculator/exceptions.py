class CalculatorError(Exception):
    """Базовое исключение калькулятора."""


class TokenizeError(CalculatorError):
    """Ошибка токенизации."""

    def __init__(self, message: str, position: int) -> None:
        super().__init__(message)
        self.position = position


class ParseError(CalculatorError):
    """Синтаксическая ошибка."""

    def __init__(self, message: str, position: int | None = None) -> None:
        super().__init__(message)
        self.position = position


class EvaluationError(CalculatorError):
    """Ошибка вычисления (неизвестная переменная, domain error и т.п.)."""
