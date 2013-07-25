pre:
	flake8 plock/*.py
	flake8 tests/*.py
	check-manifest
	pyroma .
	bin/python setup.py test
	viewdoc
