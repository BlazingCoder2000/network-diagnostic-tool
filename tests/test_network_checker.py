from network_checker import parse_input


def test_parse_simple_domain():
    domain, port, scheme = parse_input("google.com")
    assert domain == "google.com"
    assert port == "80"
    assert scheme == "http"


def test_parse_https_url():
    domain, port, scheme = parse_input("https://google.com")
    assert domain == "google.com"
    assert port == "443"
    assert scheme == "https"


def test_parse_with_port():
    domain, port, scheme = parse_input("http://example.com:8080")
    assert domain == "example.com"
    assert port == "8080"
    assert scheme == "http"
