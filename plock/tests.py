import unittest
import os.path


class PlockTests(unittest.TestCase):
    def test_create_cfg(self):
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        plock.directory = mkdtemp()
        buildout_cfg = os.path.join(plock.directory, 'buildout.cfg')
        heroku_cfg = os.path.join(plock.directory, 'heroku.cfg')
        plock.create_cfg(
            buildout_cfg,
            heroku_cfg,
            extends='https://raw.github.com/plock/pins/master/dev')
        with open(buildout_cfg, 'r') as f:
            file_contents = f.read()
        self.assertIn('https://raw.github.com/plock/pins/master/dev',
                      file_contents)

    def test_install_plone(self):
        from mock import Mock
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        args = Mock()
        args.install_dir = mkdtemp()
        args.install_addon = None
        args.list_addons = False
        args.raw = False
        args.write_only = False
        args.extends = None
        args.unified_only = False
        plock.install_plone(args, test=True)

    def test_run_buildout(self):
        from mock import Mock
        from plock.install import Installer
        plock = Installer()
        args = Mock()
        plock.run_buildout(args, test=True)


if __name__ == '__main__':
    unittest.main()
