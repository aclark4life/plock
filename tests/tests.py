def test_locale_format():
    from plock.install import Installer
    import locale
    plock = Installer()
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    result = plock.locale_format(3000)
    assert result == "3,000"
