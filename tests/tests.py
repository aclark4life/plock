from nose import with_setup


def test_locale_format():
    from plock.install import locale_format
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = locale_format(3000)
    assert result == "3,000"
