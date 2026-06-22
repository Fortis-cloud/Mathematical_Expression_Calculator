.PHONY: test lint format ci pre-commit build

test:
	pytest tests/ -v --cov=calculator --cov-fail-under=90

lint:
	ruff check calculator/ tests/
	mypy --strict calculator/

format:
	ruff format calculator/ tests/
	ruff check --fix calculator/ tests/

pre-commit:
	pre-commit run --all-files

ci: lint test build

build:
	python -m build
	twine check dist/*
