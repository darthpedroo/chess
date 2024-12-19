install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black .

lint:
	find . -name "*.py" -not -path "./.git/*" -not -path "./env/*" | xargs pylint --disable=R,C --verbose --fail-under=9.0

test:
	python -m pytest -vv --cov=business --cov-fail-under=80

all: install format lint test