from models import Dollor


def test_multiplication() -> None:
    five: Dollor = Dollor(5)
    five.times(2)
    assert five.amount == 10
