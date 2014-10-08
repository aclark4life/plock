plock
=====

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

A Plone installer for the pip-loving crowd.

.. image:: https://raw.githubusercontent.com/plock/plock/master/Plocktastic.png
    :width: 100%

Installation
------------

Plock enables the installation of Plone with pip:

::

    $ pip install plock
    $ plock .
    Creating virtualenv...
    Installing Buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.3/+download/Plone-4.3.3-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs... 
    Installing cmmi & dist...
    Configuring cache...
    Running Buildout... (this may take a while)
    Done, now run:

    ./bin/plone fg

    $ bin/plone fg

FAQ
---

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a work around for ``pip install Plone`` which technically works, but requires a lengthy requirements.txt file and is missing features provided by Buildout e.g. "instance" creation.

Why support pip? 
~~~~~~~~~~~~~~~~

To advance the state of Plone such that Buildout can be used, but not required.

Why make Buildout optional? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To market Plone to Python programmers who are generally more familiar with pip than Buildout.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_. It is also the name of a `city in Poland <http://en.wikipedia.org/wiki/P%C5%82ock>`_.
