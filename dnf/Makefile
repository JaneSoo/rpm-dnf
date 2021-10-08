all: build

build: clean
	python3 setup.py sdist

test-publish: clean build
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

publish: clean build
	twine upload dist/*

clean:
	rm -rf build dist *.egg-info

.PHONY: build publish test-publish clean
