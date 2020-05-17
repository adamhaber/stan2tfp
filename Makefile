pypi: dist
	twine upload --repository pypi dist/*

test_pypi: dist
	twine upload --repository testpypi dist/*

dist: clean
	python setup.py sdist bdist_wheel

clean:
	rm -rf dist
