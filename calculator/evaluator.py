import logging
import math
from typing import Any

from .ast_nodes import *
from .constants import CONSTANTS
from .exceptions import EvaluationError
from .functions import FUNCTION_MAP

logger = logging.getLogger("calculator.evaluator")


class Evaluator:
    def __init__(
        self,
        variables: dict[str, float | int],
        precision: int | None,
        angle_mode: str,
    ) -> None:
        self.variables = variables.copy()
        self.precision = precision
        self.angle_mode = angle_mode
        self.step = 0
        self.verbose = False

    def evaluate(self, node: ASTNode, verbose: bool = False) -> float | int:
        self.verbose = verbose
        result = node.accept(self)
        # постобработка
        if self.precision is not None:
            result = round(result, self.precision)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        return result

    def _log_step(self, operation: str, operands: list[Any], result: Any) -> None:
        if self.verbose:
            self.step += 1
            logger.debug(
                "step=%d op=%s operands=%s result=%s",
                self.step, operation, operands, result
            )

    def visit_number(self, node: NumberNode) -> float:
        return node.value

    def visit_variable(self, node: VariableNode) -> float:
        if node.name in CONSTANTS:
            return CONSTANTS[node.name]
        if node.name in self.variables:
            return self.variables[node.name]
        raise EvaluationError(f"unknown variable '{node.name}'")

    def visit_binop(self, node: BinOpNode) -> float:
        left = node.left.accept(self)
        right = node.right.accept(self)
        op = node.op
        result: float
        if op == '+':
            result = left + right
        elif op == '-':
            result = left - right
        elif op == '*':
            result = left * right
        elif op == '/':
            if right == 0:
                raise ZeroDivisionError("division by zero")
            result = left / right
        elif op == '//':
            if right == 0:
                raise ZeroDivisionError("division by zero")
            result = left // right
        elif op == '%':
            if right == 0:
                raise ZeroDivisionError("division by zero")
            result = left % right
        elif op == '**':
            # 0**0 = 1 (согласовано с Python)
            result = left ** right
        else:
            raise EvaluationError(f"unknown binary operator '{op}'")
        self._log_step(op, [left, right], result)
        return result

    def visit_unary(self, node: UnaryOpNode) -> float:
        val = node.operand.accept(self)
        op = node.op
        if op == '+':
            result = +val
        elif op == '-':
            result = -val
        elif op == '%':
            result = val / 100.0
        else:
            raise EvaluationError(f"unknown unary operator '{op}'")
        self._log_step(op, [val], result)
        return result

    def visit_function(self, node: FunctionCallNode) -> float:
        name = node.name
        if name not in FUNCTION_MAP:
            raise EvaluationError(f"unknown function '{name}'")
        args = [arg.accept(self) for arg in node.args]
        func = FUNCTION_MAP[name]

        # Проверка арности (для min/max может быть >0)
        if name in ("min", "max"):
            if len(args) == 0:
                raise EvaluationError(f"{name}() requires at least one argument")
        else:
            expected = 1 if name != "pow" else 2
            if len(args) != expected:
                from .exceptions import ParseError
                raise ParseError(
                    f"{name}() takes {expected} argument(s), got {len(args)}",
                    None   # позиция неизвестна
                )

        # Преобразование углов для тригонометрических
        if name in ("sin", "cos", "tan"):
            if self.angle_mode == "deg":
                args[0] = math.radians(args[0])

        try:
            result = func(*args)
        except ValueError as e:
            raise EvaluationError(str(e))
        self._log_step(name, args, result)
        return result

    def visit_assign(self, node: AssignmentNode) -> float:
        value = node.expr.accept(self)
        self.variables[node.name] = value
        self._log_step("assign", [node.name, value], value)
        return value

    def visit_sequence(self, node: SequenceNode) -> float:
        result = None
        for stmt in node.statements:
            result = stmt.accept(self)
        return result if result is not None else 0.0
