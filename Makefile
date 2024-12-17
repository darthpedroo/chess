install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black .

lint:
	find . -name "*.py" -not -path "./.git/*" -not -path "./env/*" | xargs pylint --disable=R,C --verbose



test:
	python -m pytest -vv --cov=business

all: install format lint test