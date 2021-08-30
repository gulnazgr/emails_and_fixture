import pytest
from helpers import log, valid_email


@pytest.mark.parametrize("email", [
    "test@test.ru",
    "w@w.com",
    "123QWE@mmm.mmm"
])
def test_valid_emails(email, log_file_name):
    log(log_file_name, f"email {email}is {'valid' if valid_email(email) else 'invalid'}")
    assert valid_email(email)


@pytest.mark.parametrize("email", [
    "test@test.",
    "w@",
    "@tt"
])
def test_invalid_emails(email, log_file_name):
    log(log_file_name, f"email {email}is {'valid' if valid_email(email) else 'invalid'}")
    assert not valid_email(email)
