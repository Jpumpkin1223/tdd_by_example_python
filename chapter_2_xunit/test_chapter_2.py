from xunit_models import WasRun


class TestCaseTest:
    def test_template_method(self) -> None:
        test = WasRun("test_method")
        test.run()
        assert "setUp testMethod tearDown " == test.log
