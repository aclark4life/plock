# encoding: utf-8
from .config import _4_3_1_CFG
from .config import ADDON_FORMAT_STRING
from .config import BASE_CFG
from .config import BUILDOUT_CFG
from .config import BUILDOUT_OPT
from .config import EXPERT_MODE
from .config import RELEASE_CFG
from .config import SEARCH_OPER
from .config import SEARCH_SPEC
from .config import argument_parser
from .config import config_parser
from .config import pypi
import collections
import locale
import os
import sh
import sys
import time


class Installer():
    """
    Plock: A Plone Installer for the Pip-Loving Crowd
    """

    def __init__(self):
        self._BACKUP = None

    def create_cfg(self):
        """
        Create Buildout config
        """
        if not os.path.exists('buildout.cfg'):

            cfg = open('4.3.1-versions.cfg', 'w')
            cfg.write(_4_3_1_CFG)
            cfg.close()

            cfg = open('base.cfg', 'w')
            cfg.write(BASE_CFG)
            cfg.close()

            cfg = open('release.cfg', 'w')
            cfg.write(RELEASE_CFG)
            cfg.close()

            cfg = open('buildout.cfg', 'w')
            cfg.write(BUILDOUT_CFG)
            cfg.close

            return True

        return False

    def create_dirs(self):
        """
        Create Buildout dirs. Match directory name with section parameter name
        e.g. download-cache = download-cache, eggs-directory = eggs-directory.
        Note: a download cache must be defined to be used; there is no
        default value, or caching enabled, if the parameter is not defined.
        Eggs directory is set by default to "eggs" if the parameter is not
        defined in buildout.cfg (which it typically is not).
        """
        dirs = ('download-cache', 'eggs-directory')
        for d in dirs:
            if not os.path.exists(d):
                os.mkdir(d)

    def install_plone(self):
        """
        Install Plone with Buildout
        """
        first_time = False
        args = argument_parser.parse_args()
        if args.add_on:
            first_time = self.install_addons(args)
        if args.list_addons:
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            if args.raw:
                self.list_addons(raw=True)
            else:
                self.list_addons()
            exit()
        if args.raw:
            print("Usage: plock --list-addons --raw")
            exit(1)

        if args.preserve and not args.install_addons:
            usage = "Usage: plock --add-on ADD_ON(S)"
            usage += " --preserve"
            print(usage)
            exit(1)

        if args.write_config:
            if self.create_cfg():
                print "Wrote buildout.cfg."
                exit(0)
            else:
                print "Failed to write buildout.cfg: it already exists."
                exit(1)

        sys.stdout.write("Installing Plone. This may take a while...")
        sys.stdout.flush()
        self.create_cfg()
        self.run_buildout()
        if first_time:
            self.install_addons(args)
        print(" done.")

    def install_addons(self, args):
        """
        Install add-ons from PyPI
        """
        if not os.path.exists('buildout.cfg'):
            # It's the first time the installer has run so we need
            # to write buildout.cfg before adding a plone section.
            # Return and come back later.
            return True

        self._BACKUP = open('buildout.cfg').read()
        addons = []
        addons.append('${base:packages}')
        addons.append('${version:packages}')
        for package in args.add_on:
            addons.append(package)
        config_parser.read('buildout.cfg')
        if not config_parser.has_section('plone'):
            config_parser.add_section('plone')
        else:
            if args.preserve:
                existing_addons = config_parser.get('plone', 'eggs')
                existing_addons = existing_addons.split('\n')

                # http://stackoverflow.com/a/1157160/185820
                existing_addons = filter(lambda a: a != u'', existing_addons)
                existing_addons = filter(
                    lambda a: a != u'${base:packages}', existing_addons)
                existing_addons = filter(
                    lambda a: a != u'${version:packages}', existing_addons)

                addons = addons + existing_addons
                addons = set(addons)
                addons = list(addons)
                addons.sort()

        config_parser.set('plone', 'eggs', '\n' + '\n'.join(addons))
        buildout_cfg = open('buildout.cfg', 'w')
        config_parser.write(buildout_cfg)
        buildout_cfg.close()

    def list_addons(self, raw=False):
        """
        List add-ons from PyPI
        """
        count = 0
        results = collections.OrderedDict()
        for package in pypi.search(SEARCH_SPEC, SEARCH_OPER):
            if 'name' in package and 'summary' in package:
                name = package['name']
                summary = package['summary']
                results[name] = summary
        for name, summary in results.items():
            count += 1
            if raw:
                print(name)
            else:
                print(
                    ADDON_FORMAT_STRING % (
                        self.locale_format(
                            count), name.ljust(40), summary.ljust(40)))

    def locale_format(self, num):
        """
        Given a number e.g. 3000 return formatted number e.g. 3,000.
        """
        try:
            return locale.format("%d", num, grouping=True)
        except TypeError:
            # XXX Keep going
            return num

    def run_buildout(self):
        buildout = sh.Command("bin/buildout")
        try:
            if EXPERT_MODE:  # Allow Buildout dirs to be
                # specified by .buildout/default.cfg
                buildout()
            else:  # Explicitly create and use Buildout dirs
                # in the current working directory.
                count = 0
                self.create_dirs()
                download = buildout(BUILDOUT_OPT, _bg=True)
                while(len(os.listdir('eggs-directory')) < 235):
                    count += 1  # Count eggs
                    num = len(os.listdir('eggs-directory'))
                    if count % 5 == 0:  # Print status
                        sys.stdout.write("(%d)" % num)
                    else:
                        time.sleep(3)
                        sys.stdout.write(".")
                    sys.stdout.flush()
                download.wait()
        except sh.ErrorReturnCode_1:
            print(" error!")
            if not self._BACKUP is None:
                buildout_cfg = open('buildout.cfg', 'w')
                buildout_cfg.write(self._BACKUP)
                buildout_cfg.close()
            exit(1)


def install():
    plock = Installer()
    plock.install_plone()
