from nose import with_setup


def test_fail():
    assert False


def test_pass():
    pass


def setup_func():
    "set up test fixtures"


def teardown_func():
    "tear down test fixtures"


@with_setup(setup_func, teardown_func)
def test():
    "test ..."
