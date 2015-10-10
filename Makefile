test:
	flake8 plock/*.py
	check-manifest
	pyroma .
	bin/python setup.py test
	viewdoc
release:
	python setup.py sdist --format=zip upload

releasetest:
	python setup.py sdist --format=zip upload -r test
