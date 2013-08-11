import unittest


class PlockTests(unittest.TestCase):

    def test_create_cfg(self):
        from plock.install import Installer
        plock = Installer()
        assert hasattr(plock, 'create_cfg')
