from models import Dollor


def test_multiplication() -> None:
    five: Dollor = Dollor(5)
    # product: Dollor = five.times(2)
    assert Dollor(10) == five.times(2)
    # product = five.times(3)
    assert Dollor(15) == five.times(3)


def test_equality() -> None:
    five: Dollor = Dollor(5)
    assert five == Dollor(5)
    assert five != Dollor(6)
