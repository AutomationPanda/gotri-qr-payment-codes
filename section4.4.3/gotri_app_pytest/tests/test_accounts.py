import pytest
from accounts import CommuterAccount

@pytest.fixture
def account():
    return CommuterAccount('a5952d78-572b-4807-9239-d67bbb6136a9')

def test_account_should_initially_be_empty(account):
    assert account.balance == 0

def test_add_money_to_the_account(account):
    account.add(25)
    assert account.balance == 25

def test_pay_some_money_from_the_account(account):
    account.add(25)
    account.pay(3)
    assert account.balance == 22

def test_pay_all_the_money_from_the_account(account):
    account.add(3)
    account.pay(3)
    assert account.balance == 0

def test_attempt_to_pay_too_much_from_the_account(account):
    account.add(2)
    with pytest.raises(ValueError):
        account.pay(3)
    assert account.balance == 2
