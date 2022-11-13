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

# build and upload to pypi and push tag to github
workflow:
	make build
	make upload
	git tag -m "v${VERSION}" v${VERSION}
	git push --tags
