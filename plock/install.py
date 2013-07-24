# encoding: utf-8
from .config import ADDON
from .config import ARGP
from .config import CFGP
from .config import CFG
from .config import CMD
from .config import EXPERT
from .config import OPER
from .config import PYPI
from .config import SPEC
import collections
import locale
import os
import sh
import sys
import time


def create_cfg():
    """
    Create Buildout config
    """
    if not os.path.exists('buildout.cfg'):
        cfg = open('buildout.cfg', 'w')
        cfg.write(CFG)
        cfg.close


def create_dirs():
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


def install():
    """
    Install Plone with Buildout
    """
    locale_format('asdf')
    args = ARGP.parse_args()
    if args.install_addons:
        install_addons(args)
    if args.list_addons:
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        list_addons()
        exit()
    sys.stdout.write("Installing Plone. This may take a while...")
    sys.stdout.flush()
    create_cfg()
    run_buildout()
    print(" done.")


def install_addons(args):
    """
    Install add-ons from PyPI
    """
    addons = []
    addons.append('${base:packages}')
    addons.append('${version:packages}')
    for package in args.install_addons:
        addons.append(package)
    CFGP.read('buildout.cfg')
    CFGP.set('plone', 'eggs', '\n' + '\n'.join(addons))
    buildout_cfg = open('buildout.cfg', 'w')
    CFGP.write(buildout_cfg)
    buildout_cfg.close()


def list_addons():
    """
    List add-ons from PyPI
    """
    count = 0
    results = collections.OrderedDict()
    for package in PYPI.search(SPEC, OPER):
        if 'name' in package and 'summary' in package:
            name = package['name']
            summary = package['summary']
            results[name] = summary
    for name, summary in results.items():
        count += 1
        print(
            ADDON % (locale_format(count), name.ljust(40), summary.ljust(40)))


def locale_format(num):
    """
    Given a number e.g. 3000 return formatted number e.g. 3,000.
    """
    try:
        return locale.format("%d", num, grouping=True)
    except TypeError:
        # XXX Keep going
        return num


def run_buildout():
    buildout = sh.Command("bin/buildout")
    try:
        if EXPERT:  # Allow Buildout dirs to be
            # specified by .buildout/default.cfg
            buildout()
        else:  # Explicitly create and use Buildout dirs
            # in the current working directory.
            create_dirs()
            download = buildout(CMD, _bg=True)
            count = 0
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
        print " error!"
        exit(1)
