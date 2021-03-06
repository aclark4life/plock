import argparse
import configparser

BUILDOUT_CFG = """\
[buildout]
extends =
    %s
"""

HEROKU_CFG = """\
[buildout]
extends =
    buildout.cfg
    https://raw.githubusercontent.com/plock/pins/master/relstorage

[plone]
http-address =
    ${env:PORT}
user =
    ${env:USERNAME}:${env:PASSWORD}
"""

REQUIREMENTS_TXT = """\
zc.buildout
"""

RAW_URL = 'https://raw.githubusercontent.com'

DEV_URL = "%s/plock/pins/master/dev" % RAW_URL
PLONE_URL = "%s/plock/pins/master/plone-5-0" % RAW_URL

INSTALLER_DIR = "Plone-5.0.5-UnifiedInstaller"
INSTALLER_URL = "https://launchpad.net/plone/5.0/5.0.5/+download/"
INSTALLER_URL += "Plone-5.0.5-UnifiedInstaller.tgz"

# http://pymotw.com/2/argparse/
argparser = argparse.ArgumentParser(
    description="Pip installs Plock. Plock installs Plone")

argparser.add_argument('install_dir', nargs='?')

argparser.add_argument("-e", "--extends", help="use additional extends file")

argparser.add_argument(
    "-f", "--force", action="store_true", help="overwrite buildout.cfg")

argparser.add_argument(
    "-i", "--install-addon", help="install add-on(s) from PyPI")

argparser.add_argument(
    "-r",
    "--raw",
    action="store_true",
    help="package name only. for use with `-l`")

argparser.add_argument(
    "-u", "--use", action="store_true", help="use existing buildout.cfg")

argparser.add_argument(
    "-w",
    "--write",
    action="store_true",
    dest="write_only",
    help="write buildout.cfg and exit")

argparser.add_argument(
    "--no-cache",
    action="store_true",
    dest="no_unified",
    help="do not download unified installer cache")

argparser.add_argument(
    "--no-buildout", action="store_true", help="do not install buildout")

argparser.add_argument(
    "--no-virtualenv", action="store_true", help="do not create virtualenv")

argparser.add_argument(
    "--cache",
    action="store_true",
    dest="unified_only",
    help="download unified installer cache and exit")

cfgparser = configparser.SafeConfigParser()
query = {'description': 'plone', 'keyword': 'plone', 'summary': 'plone'}
