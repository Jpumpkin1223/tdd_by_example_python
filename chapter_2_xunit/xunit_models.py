class TestCase:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self) -> None:
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.wasRun = False
        super().__init__(name)

    def test_method(self) -> None:
        self.wasRun = True
