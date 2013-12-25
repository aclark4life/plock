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

arg_parser.add_argument('DIRECTORY', default=os.getcwd())

arg_parser.add_argument(
    "-e", "--expert", action="store_true", help="Read .buildout/default.cfg")

arg_parser.add_argument(
    "-n", "--no-expert", action="store_true",
    help="Don't read .buildout/default.cfg")

arg_parser.add_argument(
    "-i", "--add-on", help="Install add-ons from PyPI", nargs="*")

arg_parser.add_argument(
    "-l", "--list-addons", action="store_true", help="List add-ons from PyPI")

arg_parser.add_argument(
    "-w", "--write-config", action="store_true", help="Write buildout.cfg")

# This option makes it possible to install addons (with --add-on) without
# completely
# replacing the current list of addons in buildout.cfg, which is the
# default behavior.
arg_parser.add_argument(
    "-p", "--preserve", action="store_true", help="Preserve add-ons")

arg_parser.add_argument(
    "--virtualenv", action="store_true", help="Create virtualenv")

arg_parser.add_argument(
    "-r", "--raw", action="store_true", help="Raw output")

arg_parser.add_argument(
    "-z", "--zope2-only", action="store_true", help="Install Zope2 only")

cfg_parser = configparser.SafeConfigParser()

pypi = CheeseShop()

REMOTE_PLONE = "https://raw.github.com/plock/pins/master/plone-4.3"
REMOTE_ZOPE2 = "https://raw.github.com/plock/pins/master/zope2-2.13"
