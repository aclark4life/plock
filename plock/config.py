from yolk.pypi import CheeseShop
import argparse
import configparser
import os


ADDON = "%s) %s - %s"

ARGP = argparse.ArgumentParser(
    description="Plock is a Plone Installer for the Pip-Loving Crowd")

ARGP.add_argument(
    "-i", "--install-addons", help="Install add-ons from PyPI", nargs="*")

ARGP.add_argument(
    "-l", "--list-addons", action="store_true", help="List add-ons from PyPI")

ARGP.add_argument(
    "-r", "--raw", action="store_true", help="Raw output")

EXPERT = os.environ.get('PLOCK_EXPERT')

try:
    EXPERT = eval(EXPERT)
except:
    EXPERT = False

CFG = """\
[buildout]
extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest
"""

CFGP = configparser.SafeConfigParser()

CMD = ('buildout:download-cache=download-cache',
       'buildout:eggs-directory=eggs-directory')

OPER = 'AND'

PYPI = CheeseShop()

SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
