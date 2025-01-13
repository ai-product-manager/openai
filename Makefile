install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py oalib/*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py oalib/*.py

refactor: format lint

all: install refactor test