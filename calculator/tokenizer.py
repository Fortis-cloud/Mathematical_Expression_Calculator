from enum import Enum, auto
from dataclasses import dataclass
from .exceptions import TokenizeError


class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()
    OP_PLUS = auto()
    OP_MINUS = auto()
    OP_MUL = auto()
    OP_DIV = auto()
    OP_FLOOR_DIV = auto()
    OP_MOD = auto()
    OP_POW = auto()
    LPAREN = auto()
    RPAREN = auto()
    COMMA = auto()
    SEMICOLON = auto()
    ASSIGN = auto()
    PERCENT = auto()      # постфиксный процент
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    value: str | float
    position: int


class Tokenizer:
    def __init__(self, text: str) -> None:
        self.text = text
        self.pos = 0
        self.tokens: list[Token] = []

    def tokenize(self) -> list[Token]:
        while self.pos < len(self.text):
            ch = self.text[self.pos]

            if ch.isspace():
                self.pos += 1
                continue

            if ch.isdigit() or ch == '.':
                self._read_number()
            elif ch.isalpha() or ch == '_':
                self._read_identifier()
            elif ch == '+':
                self.tokens.append(Token(TokenType.OP_PLUS, '+', self.pos))
                self.pos += 1
            elif ch == '-':
                self.tokens.append(Token(TokenType.OP_MINUS, '-', self.pos))
                self.pos += 1
            elif ch == '*':
                if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '*':
                    self.tokens.append(Token(TokenType.OP_POW, '**', self.pos))
                    self.pos += 2
                else:
                    self.tokens.append(Token(TokenType.OP_MUL, '*', self.pos))
                    self.pos += 1
            elif ch == '/':
                if self.pos + 1 < len(self.text) and self.text[self.pos + 1] == '/':
                    self.tokens.append(Token(TokenType.OP_FLOOR_DIV, '//', self.pos))
                    self.pos += 2
                else:
                    self.tokens.append(Token(TokenType.OP_DIV, '/', self.pos))
                    self.pos += 1
            elif ch == '%':
                self.tokens.append(Token(TokenType.PERCENT, '%', self.pos))
                self.pos += 1
            elif ch == '(':
                self.tokens.append(Token(TokenType.LPAREN, '(', self.pos))
                self.pos += 1
            elif ch == ')':
                self.tokens.append(Token(TokenType.RPAREN, ')', self.pos))
                self.pos += 1
            elif ch == ',':
                self.tokens.append(Token(TokenType.COMMA, ',', self.pos))
                self.pos += 1
            elif ch == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, ';', self.pos))
                self.pos += 1
            elif ch == '=':
                self.tokens.append(Token(TokenType.ASSIGN, '=', self.pos))
                self.pos += 1
            else:
                raise TokenizeError(f"unexpected character '{ch}'", self.pos)

        self.tokens.append(Token(TokenType.EOF, '', self.pos))
        return self.tokens

    def _read_number(self) -> None:
        start = self.pos
        # читаем целую часть или точку
        has_dot = False
        has_exp = False
        has_digit = False

        # знак экспоненты будет обработан отдельно
        while self.pos < len(self.text):
            ch = self.text[self.pos]
            if ch.isdigit():
                has_digit = True
                self.pos += 1
            elif ch == '_':
                # пропускаем разделитель
                self.pos += 1
            elif ch == '.':
                if has_dot:
                    break
                has_dot = True
                self.pos += 1
            elif ch in ('e', 'E'):
                if has_exp:
                    break
                has_exp = True
                self.pos += 1
                # после e может быть знак
                if self.pos < len(self.text) and self.text[self.pos] in ('+', '-'):
                    self.pos += 1
            else:
                break

        # если после e не было цифр – ошибка?
        num_str = self.text[start:self.pos].replace('_', '')
        try:
            value = float(num_str)
        except ValueError:
            raise TokenizeError(f"invalid number format '{num_str}'", start)
        self.tokens.append(Token(TokenType.NUMBER, value, start))

    def _read_identifier(self) -> None:
        start = self.pos
        while self.pos < len(self.text) and (self.text[self.pos].isalnum() or self.text[self.pos] == '_'):
            self.pos += 1
        ident = self.text[start:self.pos]
        self.tokens.append(Token(TokenType.IDENTIFIER, ident, start))
