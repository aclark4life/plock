plock
=====

Plock is a Plone Installer for the Pip-loving Crowd

.. Note:: Installing Plone with Plock requires an internet connection. If you want to install Plone offline, try `Plone's Unified Installer <http://plone.org/download>`_.

.. Warning:: Installing Plone with Plock is inherently insecure because it relies on a remote hosted configuration file(s) that in theory could be compromised during a MITM-attack.

Installation
------------

.. Note:: Plock supports the latest release (and only the latest release) of Plone, currently Plone 4.3.

Installing and running Plone with Plock looks like this::

    $ pip install plock
    $ bin/install-plone
    $ bin/plone fg

Configuration
-------------

Plone uses `Buildout <https://pypi.python.org/pypi/zc.buildout>`_ to manage its installation and configuration. Plock creates a ``buildout.cfg`` file for you that looks like this::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
    # Add-ons go here e.g.:
    #    Products.PloneFormGen

Add-ons 
~~~~~~~

.. Warning:: Plock lists packages on PyPI with a description, keyword, or summary containing "plone". Results may include packages that are not installable in the current release of Plone. This issue may be addressed in a future release of plock.

To list available add-ons::

    $ bin/install-plone --list-addons

To install add-ons, add the desired Python package name(s) to the ``eggs +=`` parameter e.g.::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
        Products.PloneFormGen

Stop Plone and run Buildout::

    $ bin/buildout

Start Plone::

    $ bin/plone fg

Install the add-on(s) in Plone via Site Setup -> Add-ons.
