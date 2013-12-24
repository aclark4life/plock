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
    "--insecure", action="store_true", help="Use online configuration files")

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

# For insecure mode, when we trust noone has altered the remote hosted
# configuration.
REMOTE_PLONE = "https://raw.github.com/plock/pins/master/plone-4.3"
REMOTE_ZOPE2 = "https://raw.github.com/plock/pins/master/zope2-2.13"

# base.cfg
BASE_PLONE = """\
[buildout]
allow-hosts =
    *.plone.org
    *.python.org
find-links =
    http://dist.plone.org/thirdparty/docutils-0.9.1.tar.gz
    http://dist.plone.org/thirdparty/elementtree-1.2.7-20070827-preview.zip
parts = plone

[base]
packages =
    Pillow
    Plone
zcml =

[plone]
eggs =
    ${base:packages}
products =
recipe = plone.recipe.zope2instance
user = admin:admin
zcml =

[versions]
# Avoid templer
ZopeSkel = 2.21.2

# Use latest; i.e higher versions than Plone core uses
Pillow = 2.1.0
zc.buildout = 2.2.0
setuptools = 0.9.8
"""

BASE_ZOPE2 = """\
[buildout]
allow-hosts =
    *.plone.org
    *.python.org
find-links =
    http://dist.plone.org/thirdparty/docutils-0.9.1.tar.gz
    http://dist.plone.org/thirdparty/elementtree-1.2.7-20070827-preview.zip
parts = zope2

[base]
packages =
    Pillow
zcml =

[zope2]
eggs =
    ${base:packages}
products =
recipe = plone.recipe.zope2instance
user = admin:admin
zcml =
    ${base:zcml}

[versions]
# Avoid templer
ZopeSkel = 2.21.2

# Use latest; i.e higher versions than Plone core uses
Pillow = 2.1.0
zc.buildout = 2.2.0
setuptools = 0.9.8
"""

# release.cfg
RELEASE_PLONE = """\
[addon]
packages =
    plonetheme.diazo_sunburst
    zope2_bootstrap
zcml =
    zope2_bootstrap

[buildout]
extends =
# The order matters
    base.cfg

[plone]
eggs =
    ${base:packages}
    ${addon:packages}
zcml =
    ${base:zcml}
    ${addon:zcml}
"""

RELEASE_ZOPE2 = """\
[addon]
packages =
    zope2_bootstrap
zcml =
    zope2_bootstrap

[buildout]
extends =
# The order matters
    base.cfg
parts = zope2

[zope2]
eggs =
    ${base:packages}
    ${addon:packages}
recipe = plone.recipe.zope2instance
user = admin:admin
zcml =
    ${base:zcml}
    ${addon:zcml}
"""
