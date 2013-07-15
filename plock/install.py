# encoding: utf-8
import os
import sh
import sys
import time

EXPERT = os.environ.get('PLOCK_EXPERT')

CFG = 'https://raw.github.com/pythonpackages/buildout-plone/master/4.3.x'

CMD1 = ('buildout:download-cache=download-cache',
        'buildout:eggs-directory=eggs-directory',
        'buildout:directory=.', '-U', '-c', CFG)

CMD2 = ('buildout:directory=.', '-c', CFG)


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
    sys.stdout.write("Installing Plone. This may take a while...")
    sys.stdout.flush()
    buildout = sh.Command("bin/buildout")
    if eval(EXPERT):  # Don't ignore .buildout.cfg
        buildout(CMD2)
    else:
        create_dirs()
        download = buildout(CMD1, _bg=True)
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
