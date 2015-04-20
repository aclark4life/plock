# encoding: utf-8
from .config import ADDON_FORMAT
from .config import ARG_PARSER
from .config import BUILDOUT_CFG
from .config import CFG_PARSER
from .config import PYPI
from .config import EXTENDS_DEV
from .config import EXTENDS_PROD
from .config import UNIFIEDINSTALLER_DIR
from .config import UNIFIEDINSTALLER_URL
from .config import SEARCH_OPER
from .config import SEARCH_SPEC
from distutils import log
import collections
import locale
import os
import sh
import shutil
import sys
import tarfile
import time
import urllib2


class Installer():
    """
    A Plone installer for the pip-loving crowd
    """

    def __init__(self):
        self.backup = None
        self.directory = None

    def add_download_cache(self):
        """
        Add downloads directory to buildout file in self.directory
        """
        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
        if os.path.exists(buildout_cfg):
            with open(buildout_cfg, "a") as myfile:
                print("Configuring cache...")
                myfile.write("download-cache=./downloads")

    def command_init(self, command):
        """
        Check to see if `command` is available to run.
        Return sh command else quit.
        """
        try:
            # Try /path/to/bin/command
            command = sh.Command(os.path.join(self.directory, "bin", command))
        except sh.CommandNotFound:
            try:
                # Try bin/command
                command = sh.Command(os.path.join("bin", command))
            except sh.CommandNotFound:
                try:
                    # Try command
                    command = sh.Command(command)
                except sh.CommandNotFound:
                    print("Error: %s command not found.\n" % command)
                    exit(1)
        return command

    def clean_up(self, test=False):
        if test:
            return
        shutil.rmtree("%s/%s" % (self.directory, UNIFIEDINSTALLER_DIR))
        shutil.rmtree("%s/buildout-cache" % self.directory)

    def create_cache(self, test=False):
        """
        Create cache directories for eggs and downloads
        """
        if test:
            return
        path_to_installer = self.download_unifiedinstaller()
        print("Unpacking installer...")
        tar = tarfile.open(path_to_installer)
        tar.extractall(self.directory)
        tar.close()

        package_folder = os.path.basename(path_to_installer)
        package_folder = package_folder.split('.tgz')[0]
        package_folder = os.path.join(self.directory, package_folder)
        path_to_cache = "%s/packages/buildout-cache.tar.bz2" % package_folder
        print("Unpacking cache...")
        tar = tarfile.open(path_to_cache)
        tar.extractall(self.directory)
        tar.close()

        buildout_cache = "%s/buildout-cache" % self.directory

        print("Installing eggs...")
        dst_eggs = "%s/eggs" % self.directory
        src_eggs = "%s/eggs" % buildout_cache
        shutil.move(src_eggs, dst_eggs)

        print("Installing cmmi & dist...")
        dst_downloads = "%s/downloads" % self.directory
        src_downloads = "%s/downloads" % buildout_cache
        shutil.move(src_downloads, dst_downloads)

    def create_cfg(self, extends=None):
        """
        Create Buildout configuration files in self.directory
        """
        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
        if not os.path.exists(buildout_cfg):
            cfg = open(buildout_cfg, 'w')
            if extends:
                wtf = BUILDOUT_CFG + '    %s\n'
                cfg.write(wtf % (EXTENDS_PROD, EXTENDS_DEV, extends))
            else:
                cfg.write(BUILDOUT_CFG % (EXTENDS_PROD, EXTENDS_DEV))
            cfg.close
        else:
            print ("Error: buildout.cfg file already exists.")
            exit(1)

    def create_venv(self):
        """
        Create virtualenv, install Buildout.
        """
        virtualenv = self.command_init("virtualenv")
        print("Creating virtualenv... (%s)" % self.directory)
        try:
            virtualenv(self.directory)
        except sh.ErrorReturnCode_1:
            print ("Error: virtualenv already exists. Try `--no-venv`")
            exit(1)

    def download_unifiedinstaller(self):
        """
        Download the unified installer
        """
        return self.download(
            package_url=UNIFIEDINSTALLER_URL,
            packagename=UNIFIEDINSTALLER_DIR,
            to_dir=self.directory
        )

    def download(
        self,
        package_url=UNIFIEDINSTALLER_URL,
        packagename=UNIFIEDINSTALLER_DIR,
        to_dir=os.curdir,
        unzip=False,
        unzip_dir=None
    ):
        """
        Download a file from a specific location. `to_dir` is the directory
        where the egg will be downloaded. Returns the location of the file.
        """
        url = package_url
        packagename = "%s.tgz" % packagename
        saveto = os.path.join(to_dir, packagename)
        src = dst = None
        if not os.path.exists(saveto):  # Avoid repeated downloads
            try:
                log.warn("Downloading installer (%s)", url)
                src = urllib2.urlopen(url)
                # Read/write all in one block, so we don't create a corrupt
                # file if the download is interrupted.
                # data = _validate_md5(egg_name, src.read())
                data = src.read()
                dst = open(saveto, "wb")
                dst.write(data)
            finally:
                if src:
                    src.close()
                if dst:
                    dst.close()
                    # XXX FIXME
                    # F821 undefined name 'unzip_package'
                    # if unzip:
                    #     unzip_package(packagename, unzip_dir)
        else:
            log.warn("Using previous download of %s", packagename)
        return os.path.realpath(saveto)

    def install_buildout(self):
        """
        Install Buildout with pip
        """
        print("Installing Buildout...")
        pip = self.command_init("pip")
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

        if not args.no_venv:
            self.create_venv()
        if not args.no_buildout:
            self.install_buildout()
        if args.unified or args.unified_only:
            self.create_cache(test=test)
        if args.extra:
            self.create_cfg(extends=args.extra)
        else:
            self.create_cfg()
        if args.unified or args.unified_only:
            self.add_download_cache()
            self.clean_up(test=test)

        if args.unified_only:
            print("Only downloading installer cache, bye!")
            exit()

        if args.install_addon:
            print("Installing addons...")
            self.install_addons(args)

        self.run_buildout(args, test=test)
        print("Done, now run:\n\n%s/bin/plone fg\n" % self.directory)

    def install_addons(self, args):
        """
        Install add-ons from PyPI
        """
        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
        self.backup = open(buildout_cfg).read()
        addons = []
        addons.append('${base:packages}')
        addons.append('${addon:packages}')
        for addon in args.install_addon.split():
            print(" %s" % addon)
            addons.append(addon)
        CFG_PARSER.read(buildout_cfg)
        CFG_PARSER.add_section('plone')
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
        for package in PYPI.search(SEARCH_SPEC, SEARCH_OPER):
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

    def run_buildout(self, args, test=False):
        if not test:
            try:
                buildout = self.command_init("buildout")
                if args.no_unified:
                    print "Running Buildout... (this may take a while)"
                else:
                    print "Running Buildout..."
                buildout(
                    "-c", os.path.join(self.directory, "buildout.cfg")
                )
            except sh.ErrorReturnCode_1:
                print("Error: Buildout run failed, restoring backup.\n")
                if self.backup is not None:
                    buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
                    cfg = open(buildout_cfg, 'w')
                    cfg.write(self.backup)
                    cfg.close()
                    self.run_buildout(args)

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
    args.unified = not args.no_unified

    plock = Installer()
    plock.install_plone(args)
