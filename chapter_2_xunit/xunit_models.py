class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        self.set_up()
        method = getattr(self, self.name)
        method()

    def set_up(self) -> None:
        pass


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.was_run = False
        self.log = ""
        super().__init__(name)

    def test_method(self) -> None:
        self.was_run = True
        self.log += "testMethod "

    def set_up(self) -> None:
        self.log = "setUp "
