class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> "TestResult":
        result = TestResult()
        result.test_started()
        self.set_up()
        try:
            method = getattr(self, self.name)
            method()
        except Exception:
            result.test_failed()
        self.tear_down()
        return result

    def set_up(self) -> None:
        pass

    def tear_down(self) -> None:
        pass


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.log = ""
        super().__init__(name)

    def set_up(self) -> None:
        self.log = "setUp "

    def test_method(self) -> None:
        self.log += "testMethod "

    def tear_down(self) -> None:
        self.log += "tearDown "

    def test_broken_method(self) -> None:
        raise Exception


class TestResult:
    def __init__(self) -> None:
        self.run_count = 0
        self.failure_count = 0

    def test_failed(self) -> None:
        self.failure_count += 1

    def test_started(self) -> None:
        self.run_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, {self.failure_count} failed"
