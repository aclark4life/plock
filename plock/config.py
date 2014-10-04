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
    "-u", "--unstable", action="store_true", help="latest release")

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

REMOTE_PLONE = "https://raw.github.com/plock/pins/master/plone-4-3"
PLONE_UNIFIEDINSTALLER = "https://launchpad.net/plone/4.3/4.3.3/+download/Plone-4.3.3-UnifiedInstaller.tgz"
PACKAGE_NAME = "Plone-4.3.3-UnifiedInstaller"

SEARCH_OPER = 'AND'
SEARCH_SPEC = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
