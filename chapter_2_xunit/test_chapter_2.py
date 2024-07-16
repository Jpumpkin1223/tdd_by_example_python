from xunit_models import TestResult, TestSuite, WasRun


class TestCaseTest:
    def test_template_method(self) -> None:
        test = WasRun("test_method")
        result = TestResult()
        test.run(result)
        assert "setUp testMethod tearDown " == test.log

    def test_result(self) -> None:
        test = WasRun("test_method")
        result = TestResult()
        test.run(result)
        assert "1 run, 0 failed" == result.summary()

    def test_failed_result(self) -> None:
        test = WasRun("test_broken_method")
        result = TestResult()
        test.run(result)
        assert "1 run, 1 failed" == result.summary()

    def test_failed_result_formatting(self) -> None:
        result = TestResult()
        result.test_started()
        result.test_failed()
        assert "1 run, 1 failed" == result.summary()

    def test_suite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun("test_method"))
        suite.add(WasRun("test_broken_method"))
        result = TestResult()
        suite.run(result)
        assert "2 run, 1 failed" == result.summary()
