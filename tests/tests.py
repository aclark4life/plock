def test_argument_parser():
    from plock.config import argument_parser
    import sys
    sys.argv = ['']  # XXX Remove "test" arg passed to setup.py
    parse_args = argument_parser.parse_args()
    for arg in ['add_on', 'list_addons', 'preserve', 'raw', 'write_config']:
        assert arg in parse_args


def test_locale_format():
    from plock.install import Installer
    import locale
    plock = Installer()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = plock.locale_format(3000)
    assert result == "3,000"
