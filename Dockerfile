FROM python:3.10-slim

WORKDIR /app

# 🔥 Install required networking tools
RUN apt-get update && apt-get install -y \
    dnsutils \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir pytest flake8

CMD ["pytest", "-v"]