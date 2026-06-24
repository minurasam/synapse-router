.PHONY: help dev install test lint type fmt bench up down clean

help:
	@echo "Targets: dev install test lint type fmt bench up down clean"

install:
	uv sync --all-extras

dev:
	uv run uvicorn synapse.main:app --reload --host 0.0.0.0 --port 8000

test:
	uv run pytest -v --cov=src/synapse --cov-report=term-missing

lint:
	uv run ruff check .

type:
	uv run mypy	src/synapse

fmt:
	uv run ruff format .
	uv run ruff check --fix .

bench:
	uv run python -m bench.run

up:
	docker compose up --build

down:
	docker compose down -v

clean:
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov
	find . -type d -name __pycache__ -exec rm -rf {} +