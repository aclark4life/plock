# encoding: utf-8
from .config import ADDON_FORMAT
from .config import ARG_PARSER
from .config import BUILDOUT_CFG
from .config import BUILDOUT_OPT
from .config import CFG_PARSER
from .config import REMOTE_PLONE
from .config import SEARCH_OPER
from .config import SEARCH_SPEC
from .config import pypi
import collections
import locale
import os
import sh
import sys
import time


class Installer():
    """
    A Plone installer for the pip-loving crowd
    """

    def __init__(self):
        self.backup = None
        self.directory = None

    def command_init(self, command, path=None):
        """
        Check to see if `command` is available to run
        """
        if path:  # Absolute
            try:
                # Try bin/command
                command = sh.Command(os.path.join(path, "bin", command))
            except sh.CommandNotFound:
                print("Error: %s command not found\n" % command)
                exit(1)
        else:  # Relative
            try:
                try:
                    # Try bin/command
                    command = sh.Command(os.path.join("bin", command))
                except sh.CommandNotFound:
                    # Try command
                    command = sh.Command(command)
            except sh.CommandNotFound:
                print("Error: %s command not found\n" % command)
                exit(1)
        return command

    def create_cfg(self):
        """
        Create Buildout configuration files in self.directory
        """
        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')

        if not os.path.exists(buildout_cfg):
            cfg = open(buildout_cfg, 'w')
            release_remote = REMOTE_PLONE
            cfg.write(BUILDOUT_CFG % release_remote)
            cfg.close
            return True
        return False

    def create_venv(self):
        """
        Create virtualenv, upgrade setuptools, install Buildout.
        """
        virtualenv = self.command_init("virtualenv")

        print("Creating virtualenv...")
        virtualenv(self.directory)

        print("Upgrading setuptools...")
        pip = self.command_init('pip', path=self.directory)
        pip('install', '--upgrade', 'setuptools')

        print("Installing Buildout...")
        pip('install', 'zc.buildout')

    def install_plone(self, args, test=False):
        """
        Install Plone with Buildout
        """

        if args.list_addons:
            if args.install_dir:
                print("Usage: plock -l")
                exit()
            locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
            if args.raw:
                self.list_addons(raw=True)
            else:
                self.list_addons()
            exit()
        if args.raw:
            print("Usage: plock --list-addons --raw")
            exit()

        if args.install_dir:
            self.directory = args.install_dir
        else:  # Quit if no install dir
            print("Usage: plock <DIR>")
            exit()

        # Create install directory if it does not exist
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)

        if args.write_config:
            if self.create_cfg():
                print "Wrote buildout.cfg."
                exit()
            else:
                print "Failed to write buildout.cfg: it already exists."
                exit(1)

        self.create_cfg()
        self.create_venv()
        if args.add_on:
            print("Installing addons...")
            self.install_addons(args)
        self.run_buildout(test=test)
        print("Done: %s/bin/plone fg\n" % self.directory)

    def install_addons(self, args):
        """
        Install add-ons from PyPI
        """

        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')

        if not os.path.exists(buildout_cfg):
            # It's the first time the installer has run so we need
            # to write buildout.cfg before adding a plone section.
            # Return and come back later.
            return True

        self.backup = open(buildout_cfg).read()
        addons = []
        addons.append('${base:packages}')
        addons.append('${addon:packages}')
        addons.append(args.add_on)
        CFG_PARSER.read('buildout.cfg')
        if not CFG_PARSER.has_section('plone'):
            CFG_PARSER.add_section('plone')

        else:
            # Preserve existing addons
            existing_addons = CFG_PARSER.get('plone', 'eggs')
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

        CFG_PARSER.set('plone', 'eggs', '\n' + '\n'.join(addons))
        cfg = open(buildout_cfg, 'w')
        CFG_PARSER.write(cfg)
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
                    ADDON_FORMAT % (
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
                buildout = self.command_init("buildout")
                BUILDOUT_OPT.append([
                    "-c", os.path.join(self.directory, "buildout.cfg")])
                print "Running Buildout (this may take a while) ..."
                buildout(
                    "-c", os.path.join(self.directory, "buildout.cfg")
                )
            except sh.ErrorReturnCode_1:
                print("Error: buildout failed.\n")
                import sys
                print sys.exc_info()[1]
                if self.backup is not None:
                    buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
                    cfg = open(buildout_cfg, 'w')
                    cfg.write(self.backup)
                    cfg.close()
                exit(1)

    def sleep(self, *args):
        if args:
            s = args[0]
        else:
            s = 9  # 10 seconds
        for i in range(s):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)


def install():
    args = ARG_PARSER.parse_args()
    plock = Installer()
    plock.install_plone(args)
