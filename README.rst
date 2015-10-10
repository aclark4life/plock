plock
=====

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

Pip installs Plock. Plock installs Plone.

.. image:: https://raw.githubusercontent.com/plock/plock/master/Plocktastic.png
    :align: center

Installation
------------

Buildout is a tool for software automation, similar to GNU Make, with INI-style configuration & written in Python. Plock uses Buildout to install Plone *without* requiring the user to have Buildout-specific knowledge or expertise, **just cut & paste**:

::

    pip install plock
    mkdir plone
    plock plone
    plone/bin/plone fg

FAQ
---

Why use pip? 
~~~~~~~~~~~~

To cater to users more familiar with pip than Buildout.

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a workaround for ``pip install Plone`` which *technically* works but requires a lengthy ``requirements.txt`` file and is missing features provided by Buildout e.g. **Zope2 instance creation**.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_. It is also the name of a `city in Poland <http://en.wikipedia.org/wiki/P%C5%82ock>`_.
