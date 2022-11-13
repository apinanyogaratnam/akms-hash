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

workflow:
	make build
	make upload
	version = $(shell python setup.py --version)
