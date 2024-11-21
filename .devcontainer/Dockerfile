FROM python:3.12.7-bookworm

WORKDIR /app

COPY pyproject.toml poetry.lock README.md .env /app/
COPY src/ /app/src/

ENV PYTHONUNBUFFERED=1 \
    PATH="/root/.local/bin:$PATH"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install

CMD tail -f /dev/null