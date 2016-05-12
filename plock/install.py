# encoding: utf-8
from distutils import log
from .config import BUILDOUT_CFG
from .config import DEV_URL
from .config import HEROKU_CFG
from .config import INSTALLER_DIR
from .config import INSTALLER_URL
from .config import PLONE_URL
from .config import argparser
from .config import cfgparser
from .config import pypi
from .config import query
import collections
import locale
import os
import sh
import shutil
import tarfile
import urllib2


class Installer():
    """
    Pip installs Plock. Plock installs Plone.
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
        """
        """
        if test:
            return
        shutil.rmtree("%s/%s" % (self.directory, INSTALLER_DIR))
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

    def create_cfg(self, buildout_cfg, heroku_cfg, extends=None):
        """
        Create buildout.cfg and heroku.cfg files in self.directory.
        """

        cfg = open(buildout_cfg, 'w')
        cfg.write(BUILDOUT_CFG % (PLONE_URL, DEV_URL))
        cfg.close()

        cfg = open(heroku_cfg, 'w')
        cfg.write(HEROKU_CFG)
        cfg.close()

        if extends:
            _extends = []
            _extends.append(PLONE_URL)
            _extends.append(DEV_URL)
            print("Configuring extends:")
            for extend in extends.split():
                print("- %s" % extend)
                _extends.append(extend)
            cfgparser.read(buildout_cfg)
            cfgparser.get('buildout', 'extends')
            cfgparser.set('buildout', 'extends', '\n' + '\n'.join(_extends))
            cfg = open(buildout_cfg, 'w')
            cfgparser.write(cfg)
            cfg.close()
            # XXX Need a better way to insert comment at ^
            cfg = open(buildout_cfg, 'r')
            chars = cfg.read()
            cfg = open(buildout_cfg, 'w')
            for line in chars.split('\n'):
                cfg.write(line.replace('\t%s' % DEV_URL, '#\t%s' % DEV_URL) +
                          '\n')
            cfg.close()

    def create_virtualenv(self):
        """
        Create virtualenv, install Buildout.
        """
        virtualenv = self.command_init("virtualenv")
        print("Creating virtualenv... (%s)" % self.directory)
        try:
            virtualenv(self.directory)
        except sh.ErrorReturnCode_1:
            print("Error: virtualenv already exists. Try `--no-virtualenv`")
            exit(1)

    def download_unifiedinstaller(self):
        """
        Download the unified installer
        """
        return self.download(package_url=INSTALLER_URL,
                             packagename=INSTALLER_DIR,
                             to_dir=self.directory)

    def download(self,
                 package_url=INSTALLER_URL,
                 packagename=INSTALLER_DIR,
                 to_dir=os.curdir,
                 unzip=False,
                 unzip_dir=None):
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
        print("Installing buildout...")
        pip = self.command_init("pip")
        pip('install', 'zc.buildout')

    def install_plone(self, args, test=False, expert=False):
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

        buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
        heroku_cfg = os.path.join(self.directory, 'heroku.cfg')
        if not (os.path.exists(buildout_cfg) or
                os.path.exists(heroku_cfg)) or args.force:
            if args.extends:
                self.create_cfg(buildout_cfg, heroku_cfg, extends=args.extends)
            else:
                self.create_cfg(buildout_cfg, heroku_cfg)
        elif args.use:
            pass
        else:
            print("Error: buildout.cfg or heroku.cfg file already exists. "
                  "Try `--force`.")
            exit(1)

        if args.write_only:
            print("Wrote buildout.cfg:\n  %s\nBye!" % buildout_cfg)
            exit(0)

        if not args.no_virtualenv:
            self.create_virtualenv()

        if not args.no_buildout:
            self.install_buildout()

        if (args.unified or args.unified_only) and not expert:
            self.create_cache(test=test)
            self.add_download_cache()
            self.clean_up(test=test)

        if args.unified_only:
            print("Only downloading installer cache, bye!")
            exit()

        if args.install_addon:
            print("Installing addons...")
            self.install_addons(args)

        error = self.run_buildout(args, test=test)
        if not error:
            print("Done, now run:\n  %s/bin/plone fg" % self.directory)

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
            print("- https://pypi.python.org/pypi/%s" % addon)
            addons.append(addon)
        cfgparser.read(buildout_cfg)
        cfgparser.add_section('plone')
        cfgparser.set('plone', 'eggs', '\n' + '\n'.join(addons))
        cfg = open(buildout_cfg, 'w')
        cfgparser.write(cfg)
        cfg.close()

    def list_addons(self, raw=False):
        """
        List add-ons from PyPI
        """
        count = 0
        results = collections.OrderedDict()
        for package in pypi.search(query, 'AND'):
            if 'name' in package and 'summary' in package:
                name = package['name']
                summary = package['summary']
                results[name] = summary
        for name, summary in results.items():
            count += 1
            if raw:
                print(name)
            else:
                print("%s) %s - %s" % (self.locale_format(count),
                                       name.ljust(40), summary.ljust(40)))

    def locale_format(self, num):
        """
        Given a number e.g. 3000 return formatted number e.g. 3,000.
        """
        try:
            return locale.format("%d", num, grouping=True)
        except TypeError:
            # XXX Keep going?
            return num

    def run_buildout(self, args, test=False):
        """
        """
        if not test:
            try:
                buildout = self.command_init("buildout")
                if args.no_unified:
                    print "Running buildout... (this may take a while)"
                else:
                    print "Running buildout..."
                buildout("-c", os.path.join(self.directory, "buildout.cfg"))
            except sh.ErrorReturnCode_1:
                print("Error: buildout run failed, restoring backup.\n")
                if self.backup is not None:
                    buildout_cfg = os.path.join(self.directory, 'buildout.cfg')
                    cfg = open(buildout_cfg, 'w')
                    cfg.write(self.backup)
                    cfg.close()
                    self.run_buildout(args)
                return (-1)

    def run_plone(self, args):
        """
        """


def install():
    """
    """
    args = argparser.parse_args()
    args.unified = not args.no_unified
    expert = False
    if 'PLOCK_EXPERT' in os.environ:
        expert = True
    plock = Installer()
    plock.install_plone(args, expert=expert)
