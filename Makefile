.PHONY: test moto setup venv

venv:
	virtualenv -p python3 venv
	. venv/bin/activate

setup: venv
	pip install -r requirements/client.txt

test:
	pytest test

moto:
	sh scripts/server.sh
