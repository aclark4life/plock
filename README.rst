plock
=====

A Plone Installer for the pip-loving Crowd

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

Installation
------------

Plock exists to enable the installation of Plone with pip.

::

    $ pip install plock
    $ plock .
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

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_.
