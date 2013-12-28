import unittest


class PlockTests(unittest.TestCase):

    def test_create_cfg(self):
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        plock.directory = mkdtemp()
        plock.create_cfg()

    def test_install_plone(self):
        from mock import Mock
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        args = Mock()
        args.install_dir = mkdtemp()
        args.add_on = None
        args.expert = False
        args.list_addons = False
        args.raw = False
        args.write_config = False
        plock.install_plone(args, test=True)

    def test_run_buildout(self):
        from plock.install import Installer
        plock = Installer()
        plock.run_buildout(test=True)


if __name__ == '__main__':
    unittest.main()
