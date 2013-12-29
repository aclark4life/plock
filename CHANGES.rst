Changelog
=========

0.1.9 (2013-12-29)
------------------

- Try bin/command before command

0.1.8 (2013-12-28)
------------------

- Support mutually exclusive options `plock .` and `plock -l`
- Restore preserve addons functionality and make it default

0.1.7 (2013-12-28)
------------------

- New features:
    - Create install_dir if it does not exist
    - Use Plock Pins instead of PythonPackages as zc.buildout configuration host
    - Add -v, --version to display version

- Bug fixes
    - Don't break --list-addons
    - Don't break --install-addons

- Removed features:
    - Remove --insecure
    - Remove --virtualenv
    - Remove --zope2-only

0.1.6 (2013-08-12)
------------------

- Bug fixes:
    - Fix Buildout command execution

0.1.5 (2013-08-12)
------------------

- Bug fixes:
    - Fix Buildout command execution

0.1.4 (2013-08-12)
------------------

- New features:
    - Add ``--expert`` command line argument, does same thing as PLOCK_EXPERT environment variable
    - Add ``--insecure`` command line argument to allow extending remote hosted configuration files
- Bug fixes:
    - Prevent inadvertently switching from Plone to Zope2 or vice versa
    - Configure Buildout command relative to current working directory, instead of relying on source bin/activate

0.1.3 (2013-07-31)
------------------

- New features:
    - Added experimental ``--zope2-only`` option to install Zope2 only.
- Bug fixes:
    - Exit Plock when egg count remains the same for longer than or equal to PLOCK_TIMEOUT

0.1.2 (2013-07-29)
------------------

- Document PLOCK_EXPERT environment variable to respect ``.buildout/default.cfg``
- Bug fixes:
    - Fixed ref to ``args.add_on`` via ``--preserve``

0.1.1 (2013-07-28)
------------------

- Fix "brown bag"

0.1.0 (2013-07-28)
------------------

- Make "secure"
    - All Buildout configuration files (for Plone, Zope2, the ZTK, etc.) are included in plock; this eliminates the possibility of a MITM-attack via remote extends (now you just need to trust PyPI and dist.plone.org.)

- Changed features:
    - Renamed script: ``install-plone`` to ``plock``.
    - Renamed arg: ``--install-addons`` to ``--add-on`` (to improve argparse-provided usage statement).

0.0.9 (2013-07-25)
------------------

- Bug fixes:
    - Don't print "Wrote buildout.cfg" if buildout.cfg exists.

0.0.8 (2013-07-25)
------------------

- New features:
    - Added --write-config to write buildout.cfg and exit.

0.0.7 (2013-07-24)
------------------

- Bug fixes:
    - Restore -U

0.0.6 (2013-07-24)
------------------

- Bug fixes:
    - Make sure addons list is sorted.

0.0.5 (2013-07-24)
------------------

- New features:
    - Added ``--raw``, for use with ``--list-addons`` e.g. bin/install-plone --list--addons --raw
    - Added ``--preserve`` for use with ``--install-addons`` e.g. bin/install-plone --install-addons Products.PloneFormGen --preserve
- Bug fixes:
    - bin/install-plone --install-addons PACKAGE(S) can now be run the first time to install both Plone and add-ons.
    - bin/install-plone --install-addons PACKAGE(S) saves a copy of buildout.cfg and reverts changes if a Buildout run fails.

0.0.4 (2013-07-23)
------------------

- Provide updated add-on installation instructions
- Install add-ons with bin/install-plone --install-addons PACKAGE(S)

0.0.3 (2013-07-22)
------------------

- List add-ons with bin/install-plone --list-addons

0.0.2 (2013-07-19)
------------------

- Provide add-on installation instructions
- Write local ``buildout.cfg`` instead of relying on -c remote_cfg.cfg

0.0.1 (2013-07-15)
------------------

- Initial release
