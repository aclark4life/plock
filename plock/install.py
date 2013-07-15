# encoding: utf-8
import os
import sh
import sys
import time


URL = 'https://raw.github.com/pythonpackages/buildout-plone/master/4.3.x'


def create_dirs():
    dirs = ('download-cache', 'eggs-directory')
    for d in dirs:
        if not os.path.exists(d):
            os.mkdir(d)


def install():
    """
    Install Plone with Buildout
    """
    sys.stdout.write("Installing Plone. This may take a while...")
    sys.stdout.flush()
    buildout = sh.Command("bin/buildout")
    create_dirs()
    download = buildout(
        'buildout:download-cache=download-cache',
        'buildout:eggs-directory=eggs-directory',
        'buildout:directory=.', '-U', '-c', URL,
        _bg=True)
    count = 0
    while(len(os.listdir('eggs-directory')) < 235):
        count += 1
        num = len(os.listdir('eggs-directory'))
        if count % 5 == 0:
            sys.stdout.write("(%d)" % num)
        else:
            time.sleep(3)
            sys.stdout.write(".")
        sys.stdout.flush()
    download.wait()
    print(" done.")
