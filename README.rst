plock
=====

.. image:: https://travis-ci.org/aclark4life/plock.png?branch=master

Pip installs Plock. Plock installs Plone.

.. image:: https://raw.githubusercontent.com/plock/plock/master/Plocktastic.png
    :align: center

Install Plone
-------------

::

    pip install plock; plock `tmp`


FAQ
---

Setuptools errors?
~~~~~~~~~~~~~~~~~~

Plock only supports the latest version of setuptools. If you're setuptools is older than the latest version, update it. You can update setuptools via::

    wget https://bootstrap.pypa.io/ez_setup.py -O - | python

See: https://pypi.python.org/pypi/setuptools#unix-wget for more installation instructions.

Missing requirements?
~~~~~~~~~~~~~~~~~~~~~

Plock only supports installation of Plone's *Python* requirements. To satisfy your operating system's requirements e.g. Ubuntu, please see:

- http://docs.plone.org/manage/installing/installation.html#install-the-operating-system-software-and-libraries-needed-to-run-plone

Why use pip? 
~~~~~~~~~~~~

Python web developers who use popular Python web frameworks (e.g. Django, Pyramid, Flask) are generally more familiar with pip than Buildout.

Why build Plock on top of Buildout? 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Plock is a workaround for ``pip install Plone`` which *technically* works but requires a lengthy ``requirements.txt`` file and is missing features provided by Buildout e.g. **Zope2 instance creation**.

Why the name Plock?
~~~~~~~~~~~~~~~~~~~

Plock is a `single by the band Plone <http://www.youtube.com/watch?v=IlLzsF61n-8>`_. It is also the name of a `city in Poland <http://en.wikipedia.org/wiki/P%C5%82ock>`_.

Plone version?
~~~~~~~~~~~~~~

Plock only supports the latest version of Plone, but with `Plock Pins <https://github.com/plock/pins>`_ you can run any version by editing the ``extends`` parameter in the ``buildout`` section in ``buildout.cfg``.
