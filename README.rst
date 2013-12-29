plock
=====

Plock is a Plone Installer for the Pip-loving Crowd

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

Installation
------------

.. Note:: Plock requires an internet connection.

.. Note:: Plock supports the latest release and only the latest release of Plone, currently Plone 4.3.

Installing and running Plone with Plock and Virtualenv looks like this::

    $ virtualenv-2.7 .
    $ source bin/activate

::

    (venv)$ pip install plock
    (venv)$ plock .
    Plock is installing Plone. This may take a while.......(3)....(4)....(4)....(4)....(5)....(5)....(9)....(14)....(21)....(24)....(29)....(33)....(38)....(43)....(48)....(54)....(58)....(62)....(66)....(71)....(74)....(78)....(78)....(83)....(87)....(89)....(92)....(97)....(98)....(98)....(98)....(98)....(98)....(100)....(102)....(103)....(108)....(110)....(113)....(115)....(120)....(123)....(128)....(133)....(138)....(142)....(148)....(153)....(158)....(161)....(163)....(168)....(171)....(175)....(179)....(181)....(184)....(189)....(193)....(195)....(198)....(203)....(205)....(210)....(214)....(221)....(224)....(228)....(234). done.

::

    (venv)$ plone fg
    2013-12-29 10:42:29 INFO ZServer HTTP server started at Sun Dec 29 10:42:29 2013
        Hostname: 0.0.0.0
        Port: 8080
    2013-12-29 10:42:36 INFO Zope Ready to handle requests

Configuration
-------------

Plone uses `Buildout <https://pypi.python.org/pypi/zc.buildout>`_ to manage its installation and configuration. Plock creates a ``buildout.cfg`` file for you that initially looks like this::

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4.3

Add-ons 
~~~~~~~

.. Warning:: Plock lists packages on PyPI with a description, keyword, or summary containing "plone". Results may include packages that are not installable in the current release of Plone. This issue may be addressed in a future release of plock.

To list available add-ons::

    $ plock --list-addons

To install add-ons, add the desired Python package name(s) to the command line e.g.::

    $ plock --add-on Products.PloneFormGen

Restart Plone and install the add-on(s) in Plone via Site Setup -> Add-ons. After you install add-ons with Plock your ``buildout.cfg`` file will look like this::

    [buildout]
    extends = release.cfg

    [plone]
    eggs = 
        ${base:packages}
        ${addon:packages}
        Products.PloneFormGen

Advanced
~~~~~~~~

Environment variables
+++++++++++++++++++++

PLOCK_EXPERT
************

If you are already familiar with ``Buildout``, you may be using a ``~/.buildout/default.cfg`` file to define various settings such as the Buildout ``eggs-directory``. In this case, you probably want to use the eggs installed in your already-defined eggs-directory (rather than letting Plock create and populate a new eggs-directory). To configure such behavior, set PLOCK_EXPERT to True e.g.::

    $ export PLOCK_EXPERT=True

Now Plock will respect your ``~/.buildout/default.cfg`` settings. Alternatively you can use the ``--expert`` command line argument to enable expert mode.

PLOCK_TIMEOUT
*************

If you are installing via a slow internet connection, you can adjust the timeout length from its default value of 45 seconds to whatever you like with the PLOCK_TIMEOUT variable::

    $ export PLOCK_TIMEOUT=60

FAQ
---

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a work around for ``pip install Plone`` which works but requires a lengthy requirements.txt, and lacks additional features provided by Buildout that are needed to use Plone. 

Why support pip? 
~~~~~~~~~~~~~~~~

To advance the state of Plone such that Buildout can be used, but not required.

Why make Buildout optional? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To market Plone to Python programmers who are generally more familiar with pip than Buildout.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_.
