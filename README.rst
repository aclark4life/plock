plock
=====

Plock is a Plone Installer for the Pip-loving Crowd

.. Note:: Installing Plone with Plock requires an internet connection. If you want to install Plone offline, try `Plone's Unified Installer <http://plone.org/download>`_.

.. Warning:: Installing Plone with Plock is inherently insecure because it relies on a remote hosted configuration file(s) that in theory could be compromised during a MITM-attack.

Installation
------------

Installing Plone with Plock looks like this::

    $ pip install plock
    $ bin/install-plone
    $ bin/plone fg

Configuration
-------------

Plock creates a ``buildout.cfg`` file for you that looks like this::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
    # Add-ons go here e.g.:
    #    Products.PloneFormGen

Add-ons
~~~~~~~

To install add-ons, add them to the ``eggs +=`` parameter e.g.::

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-plone/master/latest

    [plone]
    eggs +=
        Products.PloneFormGen

Stop Plone and run Buildout::

    $ bin/buildout

Start Plone::

    $ bin/plone fg
