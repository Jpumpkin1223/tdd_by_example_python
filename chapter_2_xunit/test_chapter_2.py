from xunit_models import WasRun


class TestCaseTest:
    def setup_method(self, _) -> None:
        self.test = WasRun("test_method")

    def test_running(self) -> None:
        self.test.run()
        assert self.test.was_run

    def test_set_up(self) -> None:
        self.test.set_up()
        assert self.test.was_set_up
