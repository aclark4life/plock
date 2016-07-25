Changelog
=========

0.6.4 (2016-07-25)
------------------

- Plone 5.0.5
- Remove DEV_URL from buildout.cfg

0.6.3 (2016-07-13)
------------------

- Fix AttributeError: 'Namespace' object has no attribute 'list_addons'

0.6.2 (2016-07-13)
------------------

- Remove yolk & list addons feature, use pip instead.

0.6.1 (2016-05-12)
------------------

- Restore PLOCK_EXPERT (set PLOCK_EXPERT to configure --no-cache default)

0.6.0 (2016-04-18)
------------------

- Add Plone 5 latest version 5.0.4

0.5.0 (2015-10-10)
------------------

- Add Plone 5 support. Since Plock only supports a single version of Plone ("latest"), Plone 5 is now the default.

0.4.4 (2015-07-04)
------------------

- Configure https://raw.githubusercontent.com/plock/pins/master/relstorage in ``heroku.cfg``

0.4.3 (2015-07-04)
------------------

- Configure ``USERNAME`` and ``PASSWORD`` env in ``heroku.cfg``

0.4.2 (2015-07-04)
------------------

- Create ``heroku.cfg``

0.4.1 (2015-07-02)
------------------

- Add ``-u, --use`` to run Plock with existing Plock buildout.cfg files.

0.4.0 (2015-06-26)
------------------

- Update GitHub content URL to https://raw.githubusercontent.com
- Rebrand: "Pip installs Plock. Plock installs Plone."
- Rename ``--write-only`` to ``--write``
- Rename ``--list-addons`` to ``--list``
- Rename ``--unified-only`` to ``--cache``
- Rename ``--no-unified`` to ``--no-cache``
- (Re)add ``--no-buildout`` option

0.3.0 (2015-04-23)
------------------

- Fix unified installer dir

0.2.9 (2015-04-23)
------------------

- (Re)add ``-w,--write-only`` option to write buildout.cfg and exit
- Add ``-f,--force`` option to overwrite existing buildout.cfg
- Remove ``--no-buildout`` option
- Support multiple extends e.g. ``-e "http://extend-one http://extend-two"``
- Add commented additional default extends https://raw.github.com/plock/pins/master/dev
- Change add-on installation syntax from ``-a, --add-on`` to ``-i, --install-addon``
- "Installing add-on" output now prints PyPI URL of add-on
- Rename ``-e, --extra`` to ``-e, --extends``

0.2.8 (2014-10-09)
------------------

- Print "this may take a while" message when ``--no-unified``.

0.2.7 (2014-10-08)
------------------

- Make ``--unified`` the default and add ``--no-unified``.
  [href]

0.2.6 (2014-10-04)
------------------

- Add ``--unified-only`` option to download Unified Installer cache & quit.

0.2.5 (2014-10-04)
------------------

- Add ``--no-buildout`` option to skip Buildout installation.

0.2.4 (2014-10-04)
------------------

- Re-add ``--no-venv`` option to allow skipping virtualenv creation.

0.2.3 (2014-10-04)
------------------
- Add ability to use Unified Installer download cache via ``--unified``.
  [pigeonflight]
- Add ability to pass an extra extends file via ``--extends``.
  [href]
- Remove ``--unstable``.
- Remove BUILDOUT_OPT

0.2.2 (2014-06-15)
------------------

- Fix bug in check_command try/except

0.2.1 (2014-06-14)
------------------

- Remove PLOCK_EXPERT
- Remove PLOCK_TIMEOUT
- Remove create_dirs
- Remove first_time
- Remove write_config
- Re-add create_venv

0.2.0 (2014-02-22)
------------------

- Change remote plone URL from https://raw.github.com/plock/pins/master/plone-4.3 to https://raw.github.com/plock/pins/master/plone-4-3

0.1.9 (2013-12-29)
------------------

- Try bin/command before command

0.1.8 (2013-12-28)
------------------

- Support mutually exclusive options ``plock .`` and ``plock -l``
- Restore preserve add-ons functionality and make it default

0.1.7 (2013-12-28)
------------------

- Create install_dir if it does not exist
- Use Plock Pins instead of PythonPackages as zc.buildout configuration host
- Add -v, ``--version`` to display version
- Bug fix: don't break ``--list-addons``
- Bug fix: don't break ``--install-addons``
- Remove ``--insecure``
- Remove ``--virtualenv``
- Remove ``--zope2-only``

0.1.6 (2013-08-12)
------------------

- Bug fix: Buildout command execution

0.1.5 (2013-08-12)
------------------

- Bug Fix: Buildout command execution

0.1.4 (2013-08-12)
------------------

- Add ``--expert`` command line argument, does same thing as PLOCK_EXPERT environment variable
- Add ``--insecure`` command line argument to allow extending remote hosted configuration files
- Bug fix: prevent inadvertently switching from Plone to Zope2 or vice versa
- Bug fix: configure Buildout command relative to current working directory, instead of relying on source bin/activate

0.1.3 (2013-07-31)
------------------

- Add experimental feature ``--zope2-only`` option to install Zope2 only.
- Bug fix: exit Plock when egg count remains the same for longer than or equal to PLOCK_TIMEOUT

0.1.2 (2013-07-29)
------------------

- Document PLOCK_EXPERT environment variable to respect ``.buildout/default.cfg``.
- Bug fix: fix reference to ``args.add_on`` via ``--preserve``.

0.1.1 (2013-07-28)
------------------

- Fix "brown bag"

0.1.0 (2013-07-28)
------------------

- Make "secure": all Buildout configuration files (for Plone, Zope2, the ZTK, etc.) are included in plock; this eliminates the possibility of a MITM-attack via remote extends (now you just need to trust PyPI and dist.plone.org.)
- Renamed script: ``install-plone`` to ``plock``.
- Renamed arg: ``--install-addons`` to ``--add-on`` (to improve argparse-provided usage statement).

0.0.9 (2013-07-25)
------------------

- Bug fix: don't print "Wrote buildout.cfg" if buildout.cfg exists.

0.0.8 (2013-07-25)
------------------

- Added ``--write-config`` to write buildout.cfg and exit.

0.0.7 (2013-07-24)
------------------

- Bug fix: re-add -U

0.0.6 (2013-07-24)
------------------

- Bug fix: sort add-ons list. 

0.0.5 (2013-07-24)
------------------

- Added ``--raw``, for use with ``--list-addons`` e.g. ``bin/install-plone --list--addons --raw``
- Added ``--preserve`` for use with ``--install-addons`` e.g. ``bin/install-plone --install-addons Products.PloneFormGen --preserve``
- Bug fix: ``bin/install-plone --install-addons PACKAGE(S)`` can now be run the first time to install both Plone and add-ons.
- Bug fix: ``bin/install-plone --install-addons PACKAGE(S)`` saves a copy of buildout.cfg and reverts changes if a Buildout run fails.

0.0.4 (2013-07-23)
------------------

- Provide updated add-on installation instructions
- Install add-ons with bin/install-plone ``--install-addons`` PACKAGE(S)

0.0.3 (2013-07-22)
------------------

- List add-ons with bin/install-plone ``--list-addons``

0.0.2 (2013-07-19)
------------------

- Provide add-on installation instructions
- Write local ``buildout.cfg`` instead of relying on -c remote_cfg.cfg

0.0.1 (2013-07-15)
------------------

- Initial release
