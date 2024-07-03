from models import Dollor, Franc


def test_dollor_multiplication() -> None:
    five: Dollor = Dollor(5)
    assert Dollor(10) == five.times(2)
    assert Dollor(15) == five.times(3)


def test_franc_multiplication() -> None:
    five: Franc = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)


def test_equality() -> None:
    assert Dollor(5) == Dollor(5)
    assert not Dollor(5) == Dollor(6)
    assert Franc(5) == Franc(5)
    assert not Franc(5) == Franc(6)
