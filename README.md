# 🧠 Network Diagnostic Tool

A Python-based network diagnostic tool designed to identify issues across DNS, network, and application layers using real system commands.

---

## 🚀 Features

- ✅ DNS resolution check (`dig`)
- ✅ Network connectivity check (`ping`)
- ✅ HTTP status check (`curl`)
- ✅ Port-aware diagnostics
- ✅ Layered issue classification (DNS / Network / Application)

---

## 🧠 How It Works

The tool follows a layered debugging approach:

```
DNS → Network → Port → Application
```

This mimics how SRE/DevOps engineers debug real production systems.

---

## 📦 Usage

Run locally:

```bash
python3 network_checker.py google.com
```

Example input:

```
http://google.com:81
```

---

## 🧪 Example Output

```
--- RESULT ---
DNS: OK
PING: OK
HTTP: UNKNOWN

--- DIAGNOSIS ---
Issue: Service/port problem
```

---

## 🛠 Tech Stack

- Python 3  
- subprocess module  
- Linux networking tools (`ping`, `dig`, `curl`)  
- Docker  
- GitHub Actions (CI/CD)  
- Pytest (Testing)  
- Flake8 (Linting)  

---

## 🐳 Docker Usage

### Build Image

```bash
docker build -t network-checker .
```

### Run Container

```bash
docker run network-checker google.com
```

---

## ☁️ DockerHub

Image available at:

```
vaibhavkakalawar/network-checker
```

Run directly:

```bash
docker run vaibhavkakalawar/network-checker google.com
```

---

## 🔄 CI/CD Pipeline

Implemented using GitHub Actions:

- Linting with flake8  
- Unit testing with pytest  
- Docker image build  
- Push to DockerHub  

Pipeline triggers on every push to `main`.

---

## 🎯 Purpose

Built as part of DevOps/SRE preparation to understand:

- Real-world network debugging  
- System-level interactions  
- Containerization with Docker  
- CI/CD workflows  

---

## 🔥 Future Improvements

- Timeout handling for network calls  
- Better HTTP status parsing  
- CLI argument support (`argparse`)  
- Structured logging  
- Deployment on AWS (ECS)  

---

## 👨‍💻 Author

Vaibhav
