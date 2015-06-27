plock
=====

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

Pip installs Plock. Plock installs Plone.

.. image:: https://raw.githubusercontent.com/plock/plock/master/Plocktastic.png
    :align: center

Installation
------------

Plock installs Plone with Buildout without requiring Buildout-specific knowledge or expertise.

::

    $ pip install plock
    $ plock .
    $ bin/plone {console,foreground}

FAQ
---

Why support pip? 
~~~~~~~~~~~~~~~~

To advance the state of Plone such that Buildout can be used but not required.

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a workaround for ``pip install Plone`` which technically works but requires a lengthy ``requirements.txt`` file and is missing features provided by Buildout *e.g. Zope2 instance creation*.

Why make Buildout optional? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To market Plone to Python programmers who are generally more familiar with pip than Buildout.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_. It is also similar to the name of a `city in Poland <http://en.wikipedia.org/wiki/P%C5%82ock>`_.
