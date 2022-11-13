.PHONY: build
VERSION = $(shell python setup.py --version)

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
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags
