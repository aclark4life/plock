def test_argument_parser_args():
    from plock.config import arg_parser
    import sys
    sys.argv = ['']  # XXX Remove "test" arg passed to setup.py
    parse_args = arg_parser.parse_args()
    args = ['add_on', 'list_addons', 'preserve', 'raw', 'write_config']
    args.append('zope2_only')
    for arg in args:
        assert arg in parse_args

    assert len(args) == len(parse_args.__dict__.keys())


def test_locale_format():
    from plock.install import Installer
    import locale
    plock = Installer()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = plock.locale_format(3000)
    assert result == "3,000"


if __name__ == '__main__':
    test_argument_parser_args()
    test_locale_format()
