#! /bin/bash

# exit if any command here fails
set -e

# activate virtual environment
source /opt/pysetup/.venv/bin/activate

# change directory to src
cd src

uvicorn main:app --host=${WEB_UVICORN_HOST}             \
                 --port ${WEB_UVICORN_PORT}             \
                 --ssl-keyfile=${SSL_KEYFILE_PATH}      \
                 --ssl-certfile=${SSL_CERTFILE_PATH}    \
                 --reload                               \
                 --proxy-headers

# to perform signals (like SIGTERM) correctly
exec "$@"
