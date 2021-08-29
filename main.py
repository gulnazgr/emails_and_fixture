import pytest


def valid_email(email):
    """
    Check is email correct
    :param email:
    :return:
    """
    import re
    return bool(re.search(r"^[\w.+\-]+@[\w]+\.[a-z]{2,3}$", email))


def log(file_name, text):
    """
    Write log to file
    :param file_name:
    :param text:
    :return:
    """
    with open(file_name, "w") as f_obj:
        f_obj.write(text)


# BEGIN

@pytest.mark.parametrize("emails, expected", [
    (["test@test.ru", "w@w.com", "123QWE@mmm.mmm"], True),
    (["test@test.", "w@", "@tt"], False)
])
def test_emails(emails, expected):
    assert all(map(valid_email, emails)) == expected, "emails test is not passed"


def test_logging(log_file_name):
    text = "test text"

    log(log_file_name, text)

    with open(log_file_name, "r") as f_obj:
        assert f_obj.read() == text, "logging is not working"

# END
