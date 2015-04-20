import unittest
import os.path


class PlockTests(unittest.TestCase):

    def test_create_cfg(self):
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        plock.directory = mkdtemp()
        plock.create_cfg(('one', 'two', 'three'))

        with open(os.path.join(plock.directory, 'buildout.cfg'), 'r') as f:
            content = f.read()

        self.assertIn('one', content)
        self.assertIn('two', content)
        self.assertIn('three', content)

    def test_install_plone(self):
        from mock import Mock
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        args = Mock()
        args.install_dir = mkdtemp()
        args.install_addon = None
        args.expert = False
        args.list_addons = False
        args.raw = False
        args.write_config = False
        args.extra = None
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
