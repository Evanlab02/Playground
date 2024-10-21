.PHONY: releases dev run format lint

releases:
	uv run ./scripts/releases.py

dev:
	python src/main.py --dev

run:
	python src/main.py

format:
	black src/
	isort src/ --profile black

lint: format
	black --check src/
	isort src/ --check-only --profile black
	flake8 src/ --max-line-length=100
	mypy src/ --strict

test:
	@pytest src/ -n 1 --cov=src/ --no-cov-on-fail --cov-report term-missing
	@coverage xml
	@coverage html
