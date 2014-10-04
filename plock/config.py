from yolk.pypi import CheeseShop
import argparse
import configparser
import pkg_resources

# http://stackoverflow.com/a/2073599/185820
_VERSION = pkg_resources.require("plock")[0].version

ADDON_FORMAT = "%s) %s - %s"

# http://pymotw.com/2/argparse/
ARG_PARSER = argparse.ArgumentParser(
    description="A Plone installer for the pip-Loving crowd",
    version=_VERSION)

ARG_PARSER.add_argument('install_dir', nargs='?')

ARG_PARSER.add_argument(
    "-a", "--add-on", help="install add-ons from PyPI")

ARG_PARSER.add_argument(
    "-l", "--list-addons", action="store_true", help="list add-ons from PyPI")

ARG_PARSER.add_argument(
    "-r", "--raw", action="store_true", help="unformatted output, use with -l")

ARG_PARSER.add_argument(
    "-u", "--unified", action="store_true", help="use unified installer egg cache")

ARG_PARSER.add_argument(
    "-e", "--extra", help="extra extends file"
)

BUILDOUT_CFG = """\
[buildout]
extends =
    %s
"""

CFG_PARSER = configparser.SafeConfigParser()

PYPI = CheeseShop()

EXTENDS = "https://raw.github.com/plock/pins/master/plone-4-3"

UNIFIEDINSTALLER_DIR = "Plone-4.3.3-UnifiedInstaller"
UNIFIEDINSTALLER_URL = "https://launchpad.net/plone/4.3/4.3.3/+download/"
UNIFIEDINSTALLER_URL += "Plone-4.3.3-UnifiedInstaller.tgz"

SEARCH_OPER = 'AND'
SEARCH_SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
