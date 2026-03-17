FROM python:3.12-slim

# Install git (and optionally build tools if needed)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run via Python so main.py can decide the port
CMD ["python", "main.py"]
