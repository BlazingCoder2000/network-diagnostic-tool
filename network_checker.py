import subprocess
from urllib.parse import urlparse


# -------- INPUT PARSING -------- #

def parse_input(user_input):
    parsed = urlparse(user_input)

    if parsed.netloc:
        host = parsed.netloc
        scheme = parsed.scheme if parsed.scheme else "http"
    else:
        host = parsed.path
        scheme = "http"

    if ":" in host:
        domain, port = host.split(":")
    else:
        domain = host
        port = "80" if scheme == "http" else "443"

    return domain, port, scheme


# -------- DNS CHECK -------- #

def check_dns(domain):
    try:
        result = subprocess.run(
            ["dig", domain],
            capture_output=True,
            text=True
        )
        return "ANSWER SECTION" in result.stdout
    except Exception:
        return False


# -------- PING CHECK -------- #

def check_ping(domain):
    try:
        result = subprocess.run(
            ["ping", "-c", "2", domain],
            capture_output=True,
            text=True
        )
        return result.returncode == 0
    except Exception:
        return False


# -------- HTTP CHECK -------- #

def check_http(domain, port, scheme):
    try:
        url = f"{scheme}://{domain}:{port}"

        result = subprocess.run(
            ["curl", "-I", url],
            capture_output=True,
            text=True
        )

        if "200" in result.stdout:
            return "OK"
        if "301" in result.stdout or "302" in result.stdout:
            return "REDIRECT"
        if "404" in result.stdout:
            return "NOT FOUND"
        if "500" in result.stdout:
            return "SERVER ERROR"

        return "UNKNOWN"

    except Exception:
        return "FAIL"


# -------- MAIN EXECUTION -------- #

def main():
    user_input = input("Enter domain or URL: ").strip()

    domain, port, scheme = parse_input(user_input)

    dns = check_dns(domain)
    ping = check_ping(domain)
    http = check_http(domain, port, scheme)

    print("\n--- RESULT ---")
    print(f"Domain: {domain}")
    print(f"Port: {port}")
    print(f"Protocol: {scheme.upper()}")

    print(f"DNS: {'OK' if dns else 'FAIL'}")
    print(f"PING: {'OK' if ping else 'FAIL'}")
    print(f"HTTP: {http}")

    print("\n--- DIAGNOSIS ---")

    if not dns:
        print("Issue: DNS failure (domain not resolved)")
    elif not ping:
        print("Issue: Network unreachable or ICMP blocked")
    elif http in ["FAIL", "UNKNOWN"]:
        print("Issue: Service/port problem or application not responding")
    elif http == "NOT FOUND":
        print("Issue: Endpoint not found (404)")
    elif http == "SERVER ERROR":
        print("Issue: Server-side error (500)")
    else:
        print("Status: Service is healthy")


if __name__ == "__main__":
    main()
    