from yolk.pypi import CheeseShop
import argparse
import configparser
import os
import pkg_resources

ADDON_FORMAT_STRING = "%s) %s - %s"

EXPERT = os.environ.get('PLOCK_EXPERT')
try:
    EXPERT = eval(EXPERT)
except TypeError, NameError:
    EXPERT = False

BUILDOUT_CFG = """\
[buildout]
extends = %s
"""

BUILDOUT_OPT = [
    'buildout:download-cache=download-cache',
    'buildout:eggs-directory=eggs-directory',
    '-U', ]

EGGS_TOTAL = 235  # Number of eggs in working set

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
arg_parser = argparse.ArgumentParser(
    description="Plock is a Plone Installer for the Pip-Loving Crowd",
    version=VERSION)

arg_parser.add_argument('install_dir', nargs='?', default=os.getcwd())

arg_parser.add_argument(
    "-e", "--expert", action="store_true", help="expert mode")

arg_parser.add_argument(
    "-a", "--add-on", help="install add-ons from PyPI")

arg_parser.add_argument(
    "-l", "--list-addons", action="store_true", help="list add-ons from PyPI")

arg_parser.add_argument(
    "-w", "--write-config", action="store_true", help="write buildout.cfg")

arg_parser.add_argument(
    "-r", "--raw", action="store_true", help="unformatted output, use with -l")

cfg_parser = configparser.SafeConfigParser()

pypi = CheeseShop()

REMOTE_PLONE = "https://raw.github.com/plock/pins/master/plone-4.3"
