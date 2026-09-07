FROM python:3.11-slim

WORKDIR /proyecto

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/
COPY tests/ ./tests/

ENV PYTHONPATH=/proyecto/app

CMD ["bash"]
