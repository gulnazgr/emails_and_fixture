from configparser import ConfigParser

import pytest


def pytest_addoption(parser):
    config_parser = ConfigParser()
    config_parser.read("config.ini")

    log_file_name = config_parser["defaults"]["log_file_name"]

    parser.addoption(
        "--log-file-name",
        action="store",
        default=log_file_name,
        help="enter log file name",
    )


@pytest.fixture
def log_file_name(request):
    """
    Fixture that returns log file name

    :param request:

    :return: Returns log file name
    :rtype: str
    """
    return request.config.getoption("--log-file-name")
