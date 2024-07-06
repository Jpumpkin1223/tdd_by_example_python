from models import Franc, Money


def test_dollor_multiplication() -> None:
    five: Money = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_franc_multiplication() -> None:
    five: Franc = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)


def test_equality() -> None:
    assert Money.dollar(5) == Money.dollar(5)
    assert not Money.dollar(5) == Money.dollar(6)
    assert Franc(5) == Franc(5)
    assert not Franc(5) == Franc(6)
    assert not Money.dollar(5) == Franc(5)
