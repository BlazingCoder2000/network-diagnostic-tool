# Network Diagnostic Tool

A Python-based network diagnostic tool designed to identify issues across DNS, network, and application layers using real system commands.

## 🚀 Features

* DNS resolution check (`dig`)
* Network connectivity check (`ping`)
* HTTP status check (`curl`)
* Port-aware diagnostics
* Clear issue classification (DNS / Network / Application)

## 🧠 How It Works

The tool follows a layered debugging approach:

```
DNS → Network → Port → Application
```

## 📦 Usage

```bash
python3 network_checker.py
```

Enter a domain or URL:

```
http://google.com:81
```

## 🧪 Example Output

```
DNS: OK
PING: OK
HTTP: UNKNOWN
Issue: Service/port problem
```

## 🛠 Tech Stack

* Python
* subprocess module
* Linux networking tools (ping, dig, curl)

## 🎯 Purpose

Built as part of DevOps/SRE preparation to understand real-world network debugging and system interactions.

## 🔥 Future Improvements

* Timeout handling
* Better HTTP status parsing
* CLI arguments support
* Logging system

---
