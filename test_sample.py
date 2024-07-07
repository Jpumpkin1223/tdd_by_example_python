from models import Bank, Expression, Money, Sum


def test_dollor_multiplication() -> None:
    five: Money = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_franc_multiplication() -> None:
    five: Money = Money.franc(5)
    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)


def test_equality() -> None:
    assert Money.dollar(5) == Money.dollar(5)
    assert not Money.dollar(5) == Money.dollar(6)
    assert Money.franc(5) == Money.franc(5)
    assert not Money.franc(5) == Money.franc(6)
    assert not Money.dollar(5) == Money.franc(5)


def test_addition() -> None:
    sum: Expression = Sum(Money.dollar(3), Money.dollar(4))
    bank: Bank = Bank()
    reduced: Money = bank.reduce(sum, "USD")
    assert Money.dollar(7) == reduced
