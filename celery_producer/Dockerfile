FROM python:3.12-slim AS base

ENV POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1

FROM base AS python-deps

COPY pyproject.toml poetry.lock ./

RUN apt-get update &&\
    apt-get -y upgrade &&\
    pip install poetry

RUN poetry install --no-root

FROM base AS runtime

COPY --from=python-deps ./.venv ./.venv
ENV PATH="/.venv/bin:$PATH"

RUN useradd --create-home appuser
USER appuser
WORKDIR /home/appuser

COPY celery_producer/app.py ./app.py

CMD ["python3", "app.py"]