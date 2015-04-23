from yolk.pypi import CheeseShop
import argparse
import configparser
import pkg_resources

EXTENDS_PROD = "https://raw.github.com/plock/pins/master/plone-4-3"
EXTENDS_DEV = "https://raw.github.com/plock/pins/master/dev"

# http://stackoverflow.com/a/2073599/185820
_VERSION = pkg_resources.require("plock")[0].version

ADDON_FORMAT = "%s) %s - %s"

# http://pymotw.com/2/argparse/
ARG_PARSER = argparse.ArgumentParser(
    description="A Plone installer for the pip-loving crowd.",
    version=_VERSION)

ARG_PARSER.add_argument('install_dir', nargs='?')

ARG_PARSER.add_argument(
    "-i", "--install-addon", help="install add-on(s) from PyPI")

ARG_PARSER.add_argument(
    "-l", "--list-addons", action="store_true", help="list add-ons from PyPI")

ARG_PARSER.add_argument(
    "-r", "--raw", action="store_true",
    help="package name only. for use with `-l`")

ARG_PARSER.add_argument(
    "--no-unified", action="store_true",
    help="do not download unified installer cache")

ARG_PARSER.add_argument(
    "-e", "--extends", help="use additional extends file")

ARG_PARSER.add_argument(
    "--no-virtualenv", action="store_true", help="do not create virtualenv")

ARG_PARSER.add_argument(
    "--unified-only", action="store_true",
    help="download unified installer cache and exit")

BUILDOUT_CFG = """\
[buildout]
extends =
    %s
#    %s
"""

CFG_PARSER = configparser.SafeConfigParser()

PYPI = CheeseShop()


UNIFIEDINSTALLER_DIR = "Plone-4.3.3-UnifiedInstaller"
UNIFIEDINSTALLER_URL = "https://launchpad.net/plone/4.3/4.3.3/+download/"
UNIFIEDINSTALLER_URL += "Plone-4.3.3-UnifiedInstaller.tgz"

SEARCH_OPER = 'AND'
SEARCH_SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
