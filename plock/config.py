from yolk.pypi import CheeseShop
import argparse
import os


ADDON = "%s) %s - %s"

ARGP = argparse.ArgumentParser(
    description="Plock is a Plone Installer for the Pip-Loving Crowd")

ARGP.add_argument(
    "-l", "--list-addons", action="store_true", help="List add-ons from PyPI")

EXPERT = os.environ.get('PLOCK_EXPERT')

try:
    EXPERT = eval(EXPERT)
except:
    EXPERT = False

CFG = """\
[buildout]
extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

[plone]
eggs +=
# Add-ons go here e.g.:
#    Products.PloneFormGen
"""

CMD = ('buildout:download-cache=download-cache',
       'buildout:eggs-directory=eggs-directory')

OPER = 'AND'

PYPI = CheeseShop()

SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
