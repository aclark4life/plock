# encoding: utf-8
from .config import ADDON_FORMAT_STRING

from .config import BUILDOUT_CFG
from .config import BUILDOUT_OPT

from .config import EGGS_TOTAL

from .config import EXPERT

# Extends
from .config import BASE_PLONE
from .config import BASE_ZOPE2

from .config import RELEASE_PLONE
from .config import RELEASE_ZOPE2

from .config import VERSIONS_CFG

# Extends (insecure)
from .config import REMOTE_PLONE
from .config import REMOTE_ZOPE2

from .config import SEARCH_OPER
from .config import SEARCH_SPEC

from .config import TIMEOUT

from .config import arg_parser
from .config import cfg_parser

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
        self.backup = None
        self.directory = None
        self.expert = EXPERT
        self.eggs_total = EGGS_TOTAL

    def create_cfg(self, insecure=False, zope2_only=False):
        """
        Create Buildout config
        """
        base_cfg = os.path.join(self.directory, 'base.cfg')
        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
        release_cfg = os.path.join(self.directory, 'release.cfg')
        versions_cfg = os.path.join(self.directory, 'versions.cfg')

        if not os.path.exists(buildout_cfg):

            if insecure:
                cfg = open(buildout_cfg, 'w')
                if zope2_only:
                    release_remote = REMOTE_ZOPE2
                else:
                    release_remote = REMOTE_PLONE
                cfg.write(BUILDOUT_CFG % release_remote)
                cfg.close

            else:
                if zope2_only:
                    BASE_CFG = BASE_ZOPE2
                    RELEASE_CFG = RELEASE_ZOPE2
                else:
                    BASE_CFG = BASE_PLONE
                    RELEASE_CFG = RELEASE_PLONE

                cfg = open(base_cfg, 'w')
                cfg.write(BASE_CFG)
                cfg.close()

                cfg = open(buildout_cfg, 'w')
                cfg.write(BUILDOUT_CFG % 'release.cfg')
                cfg.close

                cfg = open(release_cfg, 'w')
                cfg.write(RELEASE_CFG)
                cfg.close()

                cfg = open(versions_cfg, 'w')
                cfg.write(VERSIONS_CFG)
                cfg.close()
            return True
        else:
            # Don't allow --insecure if buildout.cfg already exists
            if insecure:
                print(" error: configuration exists!\n")
                print("Remove buildout.cfg and try again.")
                exit(1)

            # Prevent inadvertently switching from Plone to Zope2 or vice versa
            cfg_parser.read('release.cfg')
            if zope2_only:
                if not cfg_parser.has_section('zope2'):
                    print(" error: configuration exists.\n")
                    print("Remove buildout.cfg and try again.")
                    exit(1)
            else:
                if not cfg_parser.has_section('plone'):
                    print(" error: configuration exists.\n")
                    print("Remove buildout.cfg and try again.")
                    exit(1)

        return False

    def create_dirs(self):
        """
        Create Buildout dirs. Match directory name with section parameter name
        e.g. download-cache = download-cache, eggs-directory = eggs-directory,
        etc.

        Note: a download cache must be defined to be used; there is no
        default value, or caching enabled, if the parameter is not defined.
        Eggs directory is set by default to "eggs" if the parameter is not
        defined in buildout.cfg (which it typically is not).
        """
        dirs = ('download-cache', 'eggs-directory')
        for d in dirs:
            if not os.path.exists(d):
                os.mkdir(d)

    def install_plone(self, args, test=False):
        """
        Install Plone with Buildout
        """
        self.directory = os.path.realpath(args.DIRECTORY)
        first_time = False
        insecure = False
        zope2_only = False
        if args.add_on:
            first_time = self.install_addons(args)

        if args.expert:  # Override env var setting
            self.expert = True

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

        if args.preserve and not args.add_on:
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

        if args.zope2_only:
            zope2_only = True
            self.eggs_total = 70

        if args.insecure:
            insecure = True

        sys.stdout.write(
            "Plock is making noises. This may take a while...")
        sys.stdout.flush()

#        os.chdir(self.directory)

        self.create_cfg(insecure=insecure, zope2_only=zope2_only)
        self.run_buildout(test=test)
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

        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')

        self.backup = open(buildout_cfg).read()
        addons = []
        addons.append('${base:packages}')
        addons.append('${addon:packages}')
        for package in args.add_on:
            addons.append(package)
        cfg_parser.read('buildout.cfg')
        if not cfg_parser.has_section('plone'):
            cfg_parser.add_section('plone')
        else:
            if args.preserve:
                existing_addons = cfg_parser.get('plone', 'eggs')
                existing_addons = existing_addons.split('\n')

                # http://stackoverflow.com/a/1157160/185820
                existing_addons = filter(lambda a: a != u'', existing_addons)
                existing_addons = filter(
                    lambda a: a != u'${base:packages}', existing_addons)
                existing_addons = filter(
                    lambda a: a != u'${addon:packages}', existing_addons)

                addons = addons + existing_addons
                addons = set(addons)
                addons = list(addons)
                addons.sort()

        cfg_parser.set('plone', 'eggs', '\n' + '\n'.join(addons))
        cfg = open(buildout_cfg, 'w')
        cfg_parser.write(cfg)
        cfg.close()

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

    def run_buildout(self, test=False):
        if not test:
            try:
                # XXX Is bin/buildout a safe assumption? Probably not.
                buildout = sh.Command(os.path.join("bin", "buildout"))
            except sh.CommandNotFound:
                print(" error: buildout command not found\n")
                exit(1)
            last = []  # saved iterations
            try:
                if self.expert:  # Allow Buildout dirs to be
                    # specified by .buildout/default.cfg
                    buildout()
                else:  # Explicitly create and use Buildout dirs
                    # in the current working directory.
                    count = 0
                    self.create_dirs()
                    download = buildout(BUILDOUT_OPT, _bg=True)
                    while(len(os.listdir('eggs-directory')) < self.eggs_total):
                        count += 1  # Print status control

                        num = len(os.listdir('eggs-directory'))

                        last.append(num)
                        for value in collections.Counter(last).values():
                            if value >= TIMEOUT:
                                # If the egg count doesn't change within
                                # TIMEOUT number of saved iterations, punt!
                                print("error: taking too long!\n")
                                print("Try increasing PLOCK_TIMEOUT length.")
                                exit(1)

                        if count % 5 == 0:  # Print status
                            sys.stdout.write("(%d)" % num)
                        else:
                            time.sleep(3)
                            sys.stdout.write(".")
                        sys.stdout.flush()
                    download.wait()
            except sh.ErrorReturnCode_1:
                print(" error: buildout run failed.\n")
                print("Run buildout manually to see error.")
                if not self.backup is None:
                    buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
                    cfg = open(buildout_cfg, 'w')
                    cfg.write(self.backup)
                    cfg.close()
                exit(1)


def install():
    plock = Installer()
    args = arg_parser.parse_args()
    plock.install_plone(args)
