import subprocess
from urllib.parse import urlparse

# -------- INPUT PARSING -------- #

user_input = input("Enter domain or URL: ").strip()

parsed = urlparse(user_input)

# If scheme missing (like google.com), urlparse puts it in path
if parsed.netloc:
    host = parsed.netloc
    scheme = parsed.scheme if parsed.scheme else "http"
else:
    host = parsed.path
    scheme = "http"

# Extract domain and port
if ":" in host:
    domain, port = host.split(":")
else:
    domain = host
    port = "80" if scheme == "http" else "443"

# -------- DNS CHECK -------- #

def check_dns(domain):
    try:
        result = subprocess.run(
            ["dig", domain],
            capture_output=True,
            text=True
        )
        return "ANSWER SECTION" in result.stdout
    except:
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
    except:
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
        elif "301" in result.stdout or "302" in result.stdout:
            return "REDIRECT"
        elif "404" in result.stdout:
            return "NOT FOUND"
        elif "500" in result.stdout:
            return "SERVER ERROR"
        else:
            return "UNKNOWN"
    except:
        return "FAIL"

# -------- EXECUTION -------- #

dns = check_dns(domain)
ping = check_ping(domain)
http = check_http(domain, port, scheme)

# -------- OUTPUT -------- #

print("\n--- RESULT ---")
print(f"Domain: {domain}")
print(f"Port: {port}")
print(f"Protocol: {scheme.upper()}")

print(f"DNS: {'OK' if dns else 'FAIL'}")
print(f"PING: {'OK' if ping else 'FAIL'}")
print(f"HTTP: {http}")

# -------- DIAGNOSIS -------- #

print("\n--- DIAGNOSIS ---")

if not dns:
    print("Issue: DNS failure (domain not resolved)")
elif not ping:
    print("Issue: Network unreachable or ICMP blocked")
elif http in ["FAIL", "UNKNOWN"]:
    print("Issue: Service/port problem or application not responding")
elif http in ["NOT FOUND"]:
    print("Issue: Endpoint not found (404)")
elif http in ["SERVER ERROR"]:
    print("Issue: Server-side error (500)")
else:
    print("Status: Service is healthy")