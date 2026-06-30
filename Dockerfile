FROM python:3.12-slim

LABEL maintainer="Niran Prem"
LABEL project="GitHub CI/CD Demo"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

CMD ["gunicorn","--bind","0.0.0.0:8000","app:app"]
