from xunit_models import WasRun


def testRunning():
    test = WasRun("test_method")
    assert not test.wasRun
    test.run()
    assert test.wasRun
