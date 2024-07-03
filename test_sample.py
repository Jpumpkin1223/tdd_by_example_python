from models import Dollor


def test_multiplication() -> None:
    five: Dollor = Dollor(5)
    product: Dollor = five.times(2)
    assert product.amount == 10
    product = five.times(3)
    assert product.amount == 15


def test_equality() -> None:
    five: Dollor = Dollor(5)
    assert five.equals(Dollor(5))
    assert not five.equals(Dollor(6))
