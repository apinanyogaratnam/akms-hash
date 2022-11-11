.PHONY: build

lint:
	flake8 .

format:
	black .
	isort .

build:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/* --skip-existing
