plock
=====

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

A Plone installer for the pip-loving crowd.

.. image:: https://raw.githubusercontent.com/plock/plock/master/Plocktastic.png
    :align: center

Installation
------------

Plock enables the installation of Plone with pip [1]_:

::

    $ pip install plock
    $ plock .
    Creating virtualenv... (.)
    Installing buildout...
    Downloading installer (https://launchpad.net/plone/4.3/4.3.4/+download/Plone-4.3.4-r1-UnifiedInstaller.tgz)
    Unpacking installer...
    Unpacking cache...
    Installing eggs... 
    Installing cmmi & dist...
    Configuring cache...
    Running buildout...
    Done, now run:
      ./bin/plone fg
    $ bin/plone fg

FAQ
---

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a workaround for ``pip install Plone`` which technically works, but requires a lengthy ``requirements.txt`` file and is missing features provided by Buildout e.g. "instance" creation.

Why support pip? 
~~~~~~~~~~~~~~~~

To advance the state of Plone such that Buildout can be used, but not required.

Why make Buildout optional? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To market Plone to Python programmers who are generally more familiar with pip than Buildout.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_. It is also similar to the name of a `city in Poland <http://en.wikipedia.org/wiki/P%C5%82ock>`_.

.. [1] Sort of. Plock installs and runs Buildout for you.
