from yolk.pypi import CheeseShop
import argparse
import configparser
import os
import pkg_resources

ADDON_FORMAT = "%s) %s - %s"

BUILDOUT_CFG = """\
[buildout]
extends = %s
"""

BUILDOUT_OPT = []

SEARCH_OPER = 'AND'
SEARCH_SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}

TIMEOUT = os.environ.get('PLOCK_TIMEOUT')
try:
    TIMEOUT = eval(TIMEOUT)
except TypeError, NameError:
    TIMEOUT = 45

# http://stackoverflow.com/a/2073599/185820
VERSION = pkg_resources.require("plock")[0].version

# http://pymotw.com/2/argparse/
ARG_PARSER = argparse.ArgumentParser(
    description="A Plone installer for the pip-Loving crowd",
    version=VERSION)

ARG_PARSER.add_argument('install_dir', nargs='?')

ARG_PARSER.add_argument(
    "-a", "--add-on", help="install add-ons from PyPI")

ARG_PARSER.add_argument(
    "-l", "--list-addons", action="store_true", help="list add-ons from PyPI")

ARG_PARSER.add_argument(
    "-r", "--raw", action="store_true", help="unformatted output, use with -l")

CFG_PARSER = configparser.SafeConfigParser()

pypi = CheeseShop()

REMOTE_PLONE = "https://raw.github.com/plock/pins/master/plone-4-3"
