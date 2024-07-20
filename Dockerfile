FROM python:3.9-slim

# Install dependencies
RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
        python3-pip \
        python3-dev \
        build-essential \
        git && \
    rm -rf /var/lib/apt/lists/*

# Clone the repository
RUN git clone https://github.com/artemon87/travel_app.git /app

WORKDIR /app

# Install Python dependencies
RUN pip install --no-cache-dir -r req.txt

EXPOSE 8005

ENTRYPOINT ["python", "app.py"]
