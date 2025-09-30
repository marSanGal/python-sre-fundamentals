.PHONY: test coverage

install:
	pip install -r requirements.txt

test:
	pytest tests/

coverage:
	pytest --cov=app --cov-report=term-missing tests/

report:
	pytest --cov=app --cov-report=term-missing tests/
	open htmlcov/index.html
	
clean:
	rm -rf htmlcov .pytest_cache .coverage