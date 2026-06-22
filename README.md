# Калькулятор математических выражений

![CI](https://github.com/Fortis-cloud/math-expression-calculator/actions/workflows/ci.yml/badge.svg)
![Codecov](https://codecov.io/gh/Fortis-cloud/math-expression-calculator/branch/main/graph/badge.svg)
![PyPI](https://img.shields.io/pypi/v/math-expression-calculator.svg)

**Production-ready** библиотека для вычисления математических выражений, переданных в виде строк.  
Предназначена для использования **только как библиотека** – без CLI, REPL, веб-интерфейса, символьной алгебры и комплексных чисел.

## Особенности

- Бинарные операторы: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Унарные операторы: `+x`, `-x`, постфиксный процент `50%`
- Скобки произвольной вложенности (в пределах лимита рекурсии Python)
- Числа: целые, с плавающей точкой, научная нотация (`1.5e3`), разделители разрядов (`1_000`)
- Константы: `pi`, `e`, `tau`, `inf`
- Функции: `sqrt`, `abs`, `pow`, `min`, `max`, `floor`, `ceil`, `round`, `log`, `log10`, `ln`, `exp`, `sin`, `cos`, `tan`, `factorial`
- Переменные через словарь `variables`
- Присваивание в цепочках: `x = 2; x * 3`
- Настройка точности (`precision`), режима углов (`angle_mode`) и подробного логирования (`verbose`)
- Собственная иерархия исключений: `CalculatorError`, `TokenizeError`, `ParseError`, `EvaluationError`

## Установка

Для разработки:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
python -m pip install -U pip
python -m pip install -e .[dev]
```
## Использование

```python
from calculator import calculator, Calculator

# Простые выражения
assert calculator("2+3*4") == 14
assert calculator("sqrt(16)") == 4

# Переменные
assert calculator("x*y+1", variables={"x": 5, "y": 10}) == 51

# Тригонометрия в градусах
assert calculator("sin(90)", angle_mode="deg") == 1

# Округление
assert calculator("10/3", precision=2) == 3.33

# Присваивание
assert calculator("x = 2; x * 3", variables={}) == 6

# Использование класса Calculator
calc = Calculator(variables={"x": 10}, precision=2)
assert calc.evaluate("x / 3") == 3.33
```

## Публичный API

```python
def calculator(
    expression: str,
    *,
    verbose: bool = False,
    variables: dict[str, float | int] | None = None,
    precision: int | None = None,
    angle_mode: Literal["rad", "deg"] = "rad",
) -> int | float:
    """Вычисляет математическое выражение."""
```

## Архитектура
входная строка
→ нормализация
→ токенизация с позициями
→ рекурсивный спуск (парсер) → AST
→ вычислитель
→ постобработка (округление, приведение к int)
→ результат
---

## Лицензия

MIT License
Copyright (c) 2026 Fortis-cloud
