from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .evaluator import Evaluator


class ASTNode(ABC):
    @abstractmethod
    def accept(self, visitor: "Evaluator") -> Any:
        pass


@dataclass
class NumberNode(ASTNode):
    value: float

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_number(self)


@dataclass
class VariableNode(ASTNode):
    name: str

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_variable(self)


@dataclass
class BinOpNode(ASTNode):
    left: ASTNode
    op: str
    right: ASTNode

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_binop(self)


@dataclass
class UnaryOpNode(ASTNode):
    op: str
    operand: ASTNode

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_unary(self)


@dataclass
class FunctionCallNode(ASTNode):
    name: str
    args: list[ASTNode]

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_function(self)


@dataclass
class AssignmentNode(ASTNode):
    name: str
    expr: ASTNode

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_assign(self)


@dataclass
class SequenceNode(ASTNode):
    statements: list[ASTNode]

    def accept(self, visitor: "Evaluator") -> Any:
        return visitor.visit_sequence(self)
