plock
=====

Plock is a Plone Installer for the Pip-loving Crowd

.. Note:: Installing Plone with Plock requires an internet connection. If you want to install Plone offline, try `Plone's Unified Installer <http://plone.org/download>`_.

.. Warning:: Installing Plone with Plock is inherently insecure because it relies on a GitHub-hosted configuration file(s) that (in theory) could be compromised during a MITM-attack.

Installation
------------

Installing Plone with Plock looks like this::

    $ pip install plock
    $ bin/install-plone
    $ bin/plone fg
