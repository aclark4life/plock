# encoding: utf-8
from .config import ADDONS
from .config import ARGP
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
    Create Buildout dirs
    """
    dirs = ('download-cache', 'eggs-directory')
    for d in dirs:
        if not os.path.exists(d):
            os.mkdir(d)


def install():
    """
    Install Plone with Buildout
    """
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    args = ARGP.parse_args()
    if args.list_addons:
        list_addons()
        exit()
    sys.stdout.write("Installing Plone. This may take a while...")
    sys.stdout.flush()
    create_cfg()
    buildout = sh.Command("bin/buildout")
    if EXPERT:  # Don't ignore .buildout.cfg
        buildout()
    else:  # Ignore .buildout.cfg
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
    print(" done.")


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
            ADDONS % (locale_format(count), name.ljust(40), summary.ljust(40)))


def locale_format(num):
    """
    Given a number e.g. 3000 return formatted number e.g. 3,000.
    """
    try:
        return locale.format("%d", num, grouping=True)
    except:
        return num
