pre:
	flake8 plock/*.py
	flake8 plock/tests/*.py
	check-manifest
	pyroma .
	bin/python setup.py test
	viewdoc
