install:
	pip install --upgrade pip && pip install -r requirements.txt
install-local:
	pip install --upgrade pip && pip install -r requirements.txt -r requirements.local.txt
lint:
	pylint --disable=R,C,no-name-in-module main.py
test:
	python -m pytest -vv test_main.py