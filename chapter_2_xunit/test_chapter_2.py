from xunit_models import WasRun


class TestCaseTest:
    # def setup_method(self, _) -> None:
    #     self.test = WasRun("test_method")

    def test_template_method(self) -> None:
        self.test = WasRun("test_method")
        self.test.run()
        assert "setUp testMethod " == self.test.log
