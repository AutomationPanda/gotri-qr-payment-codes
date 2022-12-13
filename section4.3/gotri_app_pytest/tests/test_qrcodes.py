import os
import pytest
import qrcodes

# Fixtures

@pytest.fixture
def commuter_id():
    return 'a5952d78-572b-4807-9239-d67bbb6136a9'

@pytest.fixture
def security_token():
    return 'HKhLwmGWR975EAqqVx0sJ5HgLW87Q1uvTt5CrPI4'

@pytest.fixture
def filepath():
    path = 'payment_code.png'
    if os.path.isfile(path):
        os.remove(path)
    yield path
    if os.path.isfile(path):
        os.remove(path)

# Test Cases

def test_generate_a_qr_payment_code_for_a_commuter(commuter_id, security_token, filepath): 
    qrcodes.generate_payment_code(commuter_id, security_token, filepath)
    data = qrcodes.scan_payment_code(filepath)
    expected_data = commuter_id + ':' + security_token
    assert data == expected_data

def test_scanning_a_nonexistent_file_raises_a_ValueError():
    with pytest.raises(ValueError):
        qrcodes.scan_payment_code('does_not_exist.png')

@pytest.mark.parametrize(
    'cid, st, path',
    [
        (None, 'abcde', 'payment_code.png'),
        ('12345', None, 'payment_code.png'),
        ('12345', 'abcde', None)
    ]
)
def test_generating_with_null_values_raises_a_ValueError(cid, st, path):
    with pytest.raises(ValueError):
        qrcodes.generate_payment_code(cid, st, path)
