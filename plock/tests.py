import unittest


class PlockTests(unittest.TestCase):

    def test_install_plone(self):
        from mock import Mock
        from plock.install import Installer
        from tempfile import mkdtemp
        
        plock = Installer()
        mock = Mock()
        mock.DIRECTORY = mkdtemp()
        plock.install_plone(mock)


if __name__ == '__main__':
    unittest.main()
