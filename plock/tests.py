import unittest


class PlockTests(unittest.TestCase):

    def test_args(self):
        from mock import Mock
        from plock.install import Installer
        from tempfile import mkdtemp
        plock = Installer()
        args = Mock()
        args.DIRECTORY = mkdtemp()
        args.add_on = None
        args.expert = False
        args.insecure = False
        args.list_addons = False
        args.preserve = False
        args.raw = False
        args.write_config = False
        args.zope2_only = False
        plock.install_plone(args, test=True)


if __name__ == '__main__':
    unittest.main()
