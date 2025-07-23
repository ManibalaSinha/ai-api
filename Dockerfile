FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

# Change here from app:app → main:app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
