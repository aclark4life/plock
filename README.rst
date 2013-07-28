plock
=====

Plock is a Plone Installer for the Pip-loving Crowd

.. Note:: Installing Plone with Plock requires an internet connection. If you want to install Plone offline, try `Plone's Unified Installer <http://plone.org/download>`_.

.. Warning:: Installing Plone with Plock is inherently insecure because it relies on a remote hosted configuration file(s) that in theory could be compromised during a MITM-attack.

Installation
------------

.. Note:: Plock supports the latest release (and only the latest release) of Plone, currently Plone 4.3.

Installing and running Plone with Plock looks like this::

    $ virtualenv-2.7 .
    $ bin/pip install plock
    $ bin/plock
    $ bin/plone fg

Configuration
-------------

Plone uses `Buildout <https://pypi.python.org/pypi/zc.buildout>`_ to manage its installation and configuration. Plock creates a ``buildout.cfg`` file for you that (initially) looks like this::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

Add-ons 
~~~~~~~

.. Warning:: Plock lists packages on PyPI with a description, keyword, or summary containing "plone". Results may include packages that are not installable in the current release of Plone. This issue may be addressed in a future release of plock.

To list available add-ons::

    $ bin/install-plone --list-addons

To install add-ons, add the desired Python package name(s) to the command line e.g.::

    $ bin/install-plone --install-addons Products.PloneFormGen

Restart Plone and install the add-on(s) in Plone via Site Setup -> Add-ons. After you install add-ons with Plock your ``buildout.cfg`` file will look like this::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs = 
        ${base:packages}
        ${version:packages}
        Products.PloneFormGen

Why
---

Why bother building Plock on top of Buildout? Plock is a work around for ``pip install Plone`` which works but requires a lengthy requirements.txt, and lacks additional features provided by Buildout that are needed to use ``pip install Plone`` effectively.

Pip
~~~

Why bother supporting pip? To advance the state of Plone such that Buildout can be used, but not required.

Buildout
~~~~~~~~

Why make Buildout optional? To market Plone to Python Programmers who are generally more familiar with pip than Buildout.
