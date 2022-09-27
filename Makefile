VENV := .venv
AUTOFLAKE_BIN := $(VENV)/bin/autoflake
BLACK_BIN := $(VENV)/bin/black
FLAKE8_BIN := $(VENV)/bin/flake8
MYPY_BIN := $(VENV)/bin/mypy
PYTEST_BIN := $(VENV)/bin/pytest
PIPENV_RUN := pipenv run


.PHONY: test lint pytest

test: lint pytest

lint: $(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN)
	$(PIPENV_RUN) black --check .
	$(PIPENV_RUN) isort -c .
	$(PIPENV_RUN) autoflake -c -r --quiet .
	$(PIPENV_RUN) flake8 .
	$(PIPENV_RUN) mypy .

pytest: $(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN)
	$(PIPENV_RUN) pytest

fmt: $(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN)
	$(PIPENV_RUN) black .
	$(PIPENV_RUN) isort .
	$(PIPENV_RUN) autoflake --in-place --remove-unused-variables -r .

$(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN):
	pipenv install --dev
