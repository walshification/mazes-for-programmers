VENV := .venv
AUTOFLAKE_BIN := $(VENV)/bin/autoflake
BLACK_BIN := $(VENV)/bin/black
FLAKE8_BIN := $(VENV)/bin/flake8
MYPY_BIN := $(VENV)/bin/mypy
PYTEST_BIN := $(VENV)/bin/pytest
IPYTHON_BIN := $(VENV)/bin/ipython
PIPENV_RUN := pipenv run

export PIPENV_VENV_IN_PROJECT=1
export PIPENV_NO_SPIN=1


.PHONY: fmt install lint pytest shell test

test: lint pytest

lint: $(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN)
	$(PIPENV_RUN) black --check .
	$(PIPENV_RUN) isort -c .
	$(PIPENV_RUN) autoflake -c -r --quiet .
	$(PIPENV_RUN) flake8 .
	$(PIPENV_RUN) mypy .

pytest: $(PYTEST_BIN)
	$(PIPENV_RUN) pytest \
	--cov-config=setup.cfg \
	--cov=mazes \
	--cov-report html \
	--cov-report term-missing

fmt: $(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN)
	$(PIPENV_RUN) black .
	$(PIPENV_RUN) isort .
	$(PIPENV_RUN) autoflake \
	--in-place \
	--remove-unused-variables \
	--remove-all-unused-imports \
	--recursive \
	.

shell: $(IPYTHON_BIN)
	$(PIPENV_RUN) ipython

$(BLACK_BIN) $(FLAKE8_BIN) $(AUTOFLAKE_BIN) $(MYPY_BIN) $(PYTEST_BIN) $(IPYTHON_BIN):
	make install

install:
	pipenv install --dev
