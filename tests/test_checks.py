from unittest.mock import patch
from network_checker import check_dns, check_ping, check_http


# -------- DNS TEST -------- #

@patch("network_checker.subprocess.run")
def test_check_dns_success(mock_run):
    mock_run.return_value.stdout = "ANSWER SECTION"
    result = check_dns("google.com")
    assert result is True


@patch("network_checker.subprocess.run")
def test_check_dns_fail(mock_run):
    mock_run.return_value.stdout = ""
    result = check_dns("google.com")
    assert result is False


# -------- PING TEST -------- #

@patch("network_checker.subprocess.run")
def test_check_ping_success(mock_run):
    mock_run.return_value.returncode = 0
    result = check_ping("google.com")
    assert result is True


@patch("network_checker.subprocess.run")
def test_check_ping_fail(mock_run):
    mock_run.return_value.returncode = 1
    result = check_ping("google.com")
    assert result is False


# -------- HTTP TEST -------- #

@patch("network_checker.subprocess.run")
def test_check_http_200(mock_run):
    mock_run.return_value.stdout = "200 OK"
    result = check_http("google.com", "80", "http")
    assert result == "OK"


@patch("network_checker.subprocess.run")
def test_check_http_404(mock_run):
    mock_run.return_value.stdout = "404 Not Found"
    result = check_http("google.com", "80", "http")
    assert result == "NOT FOUND"


@patch("network_checker.subprocess.run")
def test_check_http_500(mock_run):
    mock_run.return_value.stdout = "500 Internal Server Error"
    result = check_http("google.com", "80", "http")
    assert result == "SERVER ERROR"
