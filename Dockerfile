# 1 layer
FROM python:3.10-alpine3.15

LABEL author="kana.suzucki@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POETRY_VIRTUALENVS_CREATE=0

WORKDIR /code

# 2 layer
RUN apk update && \
    apk add bash curl postgresql-dev gcc g++ python3-dev musl-dev && \
    pip install poetry

# 3 layer
COPY ./pyproject.toml ./

# 4 layer
RUN poetry install --no-ansi --no-interaction --no-root

# 5 layer
COPY ./entrypoint.sh ./

# 6 layer
RUN chmod +x ./entrypoint.sh

# 7 layer
COPY ./src ./
