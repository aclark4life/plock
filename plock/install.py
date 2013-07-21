# encoding: utf-8
from .config import ARGP
from .config import CFG
from .config import CMD
from .config import EXPERT
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
    args = ARGP.parse_args()
    if args.list_addons:
        print("List addons")
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
