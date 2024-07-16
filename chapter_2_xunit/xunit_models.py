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
        self.was_set_up = False
        super().__init__(name)

    def test_method(self) -> None:
        self.was_run = True

    def set_up(self) -> None:
        self.was_set_up = True
