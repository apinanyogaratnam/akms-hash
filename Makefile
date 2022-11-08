format:
	black .
	isort .

build:
	python3 setup.py sdist bdist_wheel
