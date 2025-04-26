FROM python:3.12-slim

WORKDIR /simple_app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root

RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["uvicorn", "main:simple_app", "--host", "0.0.0.0", "--port", "8000"]
