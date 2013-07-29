Changelog
=========

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
    - Added --raw, for use with --list-addons e.g. bin/install-plone --list--addons --raw
    - Added --preserve for use with --install-addons e.g. bin/install-plone --install-addons Products.PloneFormGen --preserve
- Bug fixes:
    - bin/install-plone with --install-addons PACKAGE(S) can now be run the first time to install both Plone and add-ons.
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
