def test_argument_parser_items():
    from plock.config import argument_parser
    import sys
    sys.argv = ['']  # XXX Remove "test" arg passed to setup.py
    parse_args = argument_parser.parse_args()
    for arg in ['add_on', 'list_addons', 'preserve', 'raw', 'write_config']:
        assert arg in parse_args


def test_argument_parser_preserve():
    from plock.config import argument_parser
    import sys
    sys.argv = ['-p']  # XXX Remove "test" arg passed to setup.py
    parse_args = argument_parser.parse_args()
    import pdb ; pdb.set_trace()


def test_locale_format():
    from plock.install import Installer
    import locale
    plock = Installer()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = plock.locale_format(3000)
    assert result == "3,000"


if __name__ == '__main__':
    test_argument_parser_items()
    test_argument_parser_preserve()
    test_locale_format()
