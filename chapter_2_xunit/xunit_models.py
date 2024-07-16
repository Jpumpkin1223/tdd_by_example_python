class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.was_run = False
        super().__init__(name)

    def test_method(self) -> None:
        self.was_run = True
