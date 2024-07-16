from xunit_models import WasRun


class TestCaseTest:
    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def test_result(self) -> None:
        test = WasRun("test_method")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()
