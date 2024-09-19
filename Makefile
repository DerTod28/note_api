.PHONY: all help clean line_code run pep8 qa flush

# target: all - Default target. Does nothing.
all:
	@clear
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@clear
	@egrep "^# target:" [Mm]akefile

# target: clean - Delete pycache
clean:
	echo "### Cleaning *.pyc and .DS_Store files "
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name '.DS_Store' -exec rm -f {} \;
	find . -name "__pycache__" -type d -exec rm -rf {} +

# target: line_code - counting lines of code
line_code:
	echo "### Counting lines of code within the project"
	echo "# Python:" ; find . -name '*.py' -type f -exec cat {} + | wc -l
	echo "# JavaScript:" ; find . -name '*.js' -type f -exec cat {} + | wc -l
	echo "# HTML:" ; find . -name '*.html' -type f -exec cat {} + | wc -l
	echo "# CSS:" ; find . -name '*.css' -type f -exec cat {} + | wc -l

# target: run - Run server
run:
	uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload

# target: mypy - Run static typing
mypy:
	mypy --config-file=mypy.ini app --no-incremental

# target: pylint - Checks for errors, enforces a coding standard, looks for code smells.
pylint:
	pylint app

# target: pep8 - Run code style test
pep8:
	flake8 app --config=setup.cfg

# target: isort - Sorts imports
isort:
	isort app

# target: black - Code formatting
black:
	black app

# target: all in one formatters
fmt: isort black

# target: all in one lints
lint: black mypy pylint pep8

# target: qa - Run tests
qa:
	pytest
