from xunit_models import WasRun


def test_running():
    test = WasRun("test_method")
    assert not test.was_run
    test.run()
    assert test.was_run


# def test