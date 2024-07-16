from xunit_models import WasRun


def test_running() -> None:
    test = WasRun("test_method")
    assert not test.was_run
    test.run()
    assert test.was_run


def test_set_up() -> None:
    test = WasRun("test_method")
    test.run()
    assert test.was_set_up
