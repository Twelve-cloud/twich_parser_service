# ---------------------------------------------------------------------------
# python-base stage sets up all shared environment variables.
FROM python:3.10-alpine3.15 as python-base

ENV                                                                         \
    # force stdout and stderr streams to be unbuffered.
    PYTHONUNBUFFERED=1                                                      \
    # prevents python from creating .pyc files.
    PYTHONDONTWRITEBYTECODE=1                                               \
    # disable pip cache.
    PIP_NO_CACHE_DIR=0                                                      \
    # disable periodically checking PyPI for a new version of pip.
    PIP_DISABLE_PIP_VERSION_CHECK=1                                         \
    # set the default socket timeout.
    PIP_DEFAULT_TIMEOUT=100                                                 \
    # poetry version.
    POETRY_VERSION=1.8.0                                                    \
    # make poetry create the virtual environment in the project's root.
    POETRY_VIRTUALENVS_IN_PROJECT=1                                         \
    # make poetry to be installed into this location.
    POETRY_HOME="/opt/poetry"                                               \
    # this is where requirements will live.
    PYSETUP_PATH="/opt/pysetup"                                             \
    # this is where venv will live.
    VENV_PATH="/opt/pysetup/.venv"

ENV                                                                         \
    # prepend poetry and venv to path.
    # this allows to use poetry without specifying full path.
    # this allows to use python from venv without using poetry shell.
    # this is so because python will be used as $VENV_PATH/bin/python.
    PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# ---------------------------------------------------------------------------
# builder-base stage installs all necessary core deps.
FROM python-base as builder-base

# install core deps.
RUN apk update                                                              \
    && apk add                                                              \
    bash                                                                    \
    curl                                                                    \
    gcc                                                                     \
    g++                                                                     \
    musl-dev                                                                \
    postgresql-dev                                                          \
    python3-dev

# ---------------------------------------------------------------------------
# poetry-base stage installs poetry, creates venv and installs project deps.
FROM python-base as poetry-base

# install curl to download poetry.
RUN apk update && apk add curl

# install poetry with respect $POETRY_VERSION & $POETRY_HOME.
RUN curl -sSL https://install.python-poetry.org | python3

# set working directory.
WORKDIR $PYSETUP_PATH

# copy project requirement files here to ensure they will be cached.
COPY pyproject.toml poetry.lock ./

# install deps ($POETRY_VIRTUALENVS_IN_PROJECT used internally).
RUN poetry install --no-ansi --no-interaction --only main

# ---------------------------------------------------------------------------
# development stage is used during development / testing.
FROM builder-base as development

# copy poetry to development stage.
COPY --from=poetry-base $POETRY_HOME $POETRY_HOME

# copy venv to development stage.
COPY --from=poetry-base $PYSETUP_PATH $PYSETUP_PATH

# set working directory.
WORKDIR $PYSETUP_PATH

# install dev deps (other deps are already installed).
RUN poetry install --no-ansi --no-interaction

# set working directory (will be mountpoint - src should be mounted).
WORKDIR /code

# copy entrypoint of the project to workdir.
COPY ./entrypoint.sh ./

# set entrypoint of the project.
ENTRYPOINT ["./entrypoint.sh"]

# container will listen this port.
EXPOSE 443

# ---------------------------------------------------------------------------
# production stage is used for runtime.
FROM builder-base as production

# copy venv to production stage.
COPY --from=poetry-base $PYSETUP_PATH $PYSETUP_PATH

# create sys group named "non-root-user".
RUN addgroup -S non-root-user

# create sys user named "non-root-user" and add it to group "non-root-user".
RUN adduser -S non-root-user non-root-user

# set working directory.
WORKDIR /code

# change the ownershup of the workdir to the non-root user "non-root-user".
RUN chown -R non-root-user:non-root-user /code

# switch to the non-root user "non-root-user".
USER non-root-user

# copy source code of the project to workdir/src.
COPY ./src ./src

# copy entrypoint of the project to workdir.
COPY ./entrypoint.sh ./

# set entrypoint of the project.
ENTRYPOINT ["./entrypoint.sh"]

# container will listen this port.
EXPOSE 443
