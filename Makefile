install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

test:
	python -m pytest -cov test_main.py

format:	
	black *.py 

lint:
	ruff check *.py mylib/*.py

generate_and_push:
	python main.py
	git config --local user.email "action@github.com"
	git config --local user.name "GitHub Action"
	git checkout -- CancerDB.db
	git pull
	git add .
	git commit -m "rerun push" --allow-empty
	git push

all: install lint test format generate_and_push