import logging
from .tokenizer import Tokenizer
from .parser import Parser
from .evaluator import Evaluator
from .exceptions import TokenizeError, ParseError


def evaluate(
    expression: str,
    variables: dict[str, float | int],
    precision: int | None,
    angle_mode: str,
    verbose: bool,
) -> float | int:
    if not expression or not expression.strip():
        raise ValueError("empty expression")

    # Настройка логирования
    if verbose:
        logger = logging.getLogger("calculator.evaluator")
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            formatter = logging.Formatter("DEBUG %(name)s: %(message)s")
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.propagate = False

    # Токенизация
    tokenizer = Tokenizer(expression)
    try:
        tokens = tokenizer.tokenize()
    except TokenizeError as e:
        raise

    # Парсинг
    parser = Parser(tokens)
    try:
        ast = parser.parse()
    except ParseError as e:
        raise

    # Вычисление
    evaluator = Evaluator(variables, precision, angle_mode)
    result = evaluator.evaluate(ast, verbose)

    return result
