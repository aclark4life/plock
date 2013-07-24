from yolk.pypi import CheeseShop
import argparse
import configparser
import os

ADDON_FORMAT_STRING = "%s) %s - %s"

EXPERT = os.environ.get('PLOCK_EXPERT')

try:
    EXPERT = eval(EXPERT)
except:
    EXPERT = False

BUILDOUT_CFG = """\
[buildout]
extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest
"""

CMD = ('buildout:download-cache=download-cache',
       'buildout:eggs-directory=eggs-directory')

OPER = 'AND'

PYPI = CheeseShop()

SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}

argument_parser = argparse.ArgumentParser(
    description="Plock is a Plone Installer for the Pip-Loving Crowd")

argument_parser.add_argument(
    "-i", "--install-addons", help="Install add-ons from PyPI", nargs="*")

argument_parser.add_argument(
    "-l", "--list-addons", action="store_true", help="List add-ons from PyPI")

argument_parser.add_argument(
    "-r", "--raw", action="store_true", help="Raw output")

config_parser = configparser.SafeConfigParser()
