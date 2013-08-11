pre:
	flake8 plock/*.py
	check-manifest
	pyroma .
	bin/python setup.py test
	viewdoc
