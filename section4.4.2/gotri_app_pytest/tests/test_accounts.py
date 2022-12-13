from accounts import CommuterAccount

def test_account_should_initially_be_empty():

    # Given a commuter has a valid ID
    commuter_id = 'a5952d78-572b-4807-9239-d67bbb6136a9'

    # When an account is created for the commuter
    account = CommuterAccount(commuter_id)

    # Then the account has an empty balance
    assert account.balance == 0