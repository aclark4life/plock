from yolk.pypi import CheeseShop
import argparse
import configparser
import pkg_resources

# http://stackoverflow.com/a/2073599/185820
_VERSION = pkg_resources.require("plock")[0].version

BUILDOUT_CFG = """\
[buildout]
extends =
    %s
#    %s
"""

PLOCK_PLONE_4_3_URL = "https://raw.github.com/plock/pins/master/plone-4-3"
PLOCK_PLONE_DEV_URL = "https://raw.github.com/plock/pins/master/dev"
UNIFIEDINSTALLER_DIR = "Plone-4.3.4-UnifiedInstaller"
UNIFIEDINSTALLER_URL = "https://launchpad.net/plone/4.3/4.3.4/+download/"
UNIFIEDINSTALLER_URL += "Plone-4.3.4-r1-UnifiedInstaller.tgz"

# http://pymotw.com/2/argparse/
argparser = argparse.ArgumentParser(
    description="A Plone installer for the pip-loving crowd.",
    version=_VERSION)

argparser.add_argument('install_dir', nargs='?')

argparser.add_argument(
    "-e", "--extends", help="extend config")

argparser.add_argument(
    "-f", "--force", action="store_true", help="overwrite config")

argparser.add_argument(
    "-i", "--install", help="install add-on")

argparser.add_argument(
    "-l", "--list", action="store_true", help="list add-ons")

argparser.add_argument(
    "-r", "--raw", action="store_true",
    help="disable formatting")

argparser.add_argument(
    "-w", "--write", action="store_true",
    help="write config & quit")

argparser.add_argument(
    "--no-cache", action="store_true",
    help="no download cache")

argparser.add_argument(
    "--no-buildout", action="store_true", help="no install buildout")

argparser.add_argument(
    "--no-virtualenv", action="store_true", help="no create virtualenv")

argparser.add_argument(
    "--cache", action="store_true",
    help="download cache & quit")

cfgparser = configparser.SafeConfigParser()
pypi = CheeseShop()
query = {
    'description': 'plone',
    'keyword': 'plone',
    'summary': 'plone'
}
