from .tokenizer import Token, TokenType, Tokenizer
from .ast_nodes import *
from .exceptions import ParseError


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.pos = 0

    def parse(self) -> ASTNode:
        return self._program()

    def _peek(self) -> Token:
        return self.tokens[self.pos]

    def _consume(self, expected_type: TokenType | None = None) -> Token:
        tok = self._peek()
        if expected_type is not None and tok.type != expected_type:
            raise ParseError(
                f"expected {expected_type.name}, got {tok.type.name}",
                tok.position
            )
        self.pos += 1
        return tok

    def _match(self, *types: TokenType) -> bool:
        return self._peek().type in types

    # program = { statement } ;
    def _program(self) -> ASTNode:
        stmts = []
        while self._peek().type != TokenType.EOF:
            stmts.append(self._statement())
            if self._match(TokenType.SEMICOLON):
                self._consume(TokenType.SEMICOLON)
            else:
                break
        if len(stmts) == 1:
            return stmts[0]
        return SequenceNode(stmts)

    # statement = assignment | expression ;
    def _statement(self) -> ASTNode:
        # Проверка на присваивание: IDENTIFIER '='
        if self._peek().type == TokenType.IDENTIFIER:
            # заглядываем на один токен вперёд
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == TokenType.ASSIGN:
                ident = self._consume(TokenType.IDENTIFIER)
                self._consume(TokenType.ASSIGN)
                expr = self._expression()
                return AssignmentNode(ident.value, expr)
        return self._expression()

    # expression = term { ("+" | "-") term } ;
    def _expression(self) -> ASTNode:
        node = self._term()
        while self._match(TokenType.OP_PLUS, TokenType.OP_MINUS):
            op = self._consume()
            right = self._term()
            node = BinOpNode(node, op.value, right)
        return node

    # term = factor { ("*" | "/" | "//" | "%") factor } ;
    def _term(self) -> ASTNode:
        node = self._factor()
        while self._match(TokenType.OP_MUL, TokenType.OP_DIV, TokenType.OP_FLOOR_DIV, TokenType.OP_MOD):
            op = self._consume()
            right = self._factor()
            node = BinOpNode(node, op.value, right)
        return node

    # factor = power { "**" power } ;  (правоассоциативно)
    def _factor(self) -> ASTNode:
        left = self._unary()
        if self._match(TokenType.OP_POW):
            self._consume(TokenType.OP_POW)
            right = self._factor()   # правоассоциативность
            return BinOpNode(left, '**', right)
        return left

    # unary = ("+" | "-") unary | postfix ;
    def _unary(self) -> ASTNode:
        if self._match(TokenType.OP_PLUS, TokenType.OP_MINUS):
            op = self._consume()
            operand = self._unary()
            return UnaryOpNode(op.value, operand)
        return self._postfix()

    # postfix = primary [ "%" ] ;
    def _postfix(self) -> ASTNode:
        node = self._primary()
        if self._match(TokenType.PERCENT):
            self._consume(TokenType.PERCENT)
            node = UnaryOpNode('%', node)
        return node

    # primary = NUMBER | IDENTIFIER | function_call | "(" expression ")" ;
    def _primary(self) -> ASTNode:
        tok = self._peek()
        if tok.type == TokenType.NUMBER:
            self._consume()
            return NumberNode(float(tok.value))
        elif tok.type == TokenType.IDENTIFIER:
            ident = self._consume()
            if self._match(TokenType.LPAREN):
                # function call
                self._consume(TokenType.LPAREN)
                args = []
                if not self._match(TokenType.RPAREN):
                    args.append(self._expression())
                    while self._match(TokenType.COMMA):
                        self._consume(TokenType.COMMA)
                        args.append(self._expression())
                self._consume(TokenType.RPAREN)
                return FunctionCallNode(ident.value, args)
            else:
                return VariableNode(ident.value)
        elif tok.type == TokenType.LPAREN:
            self._consume(TokenType.LPAREN)
            expr = self._expression()
            self._consume(TokenType.RPAREN)
            return expr
        else:
            raise ParseError(f"unexpected token {tok.type.name}", tok.position)
