#! /bin/bash

# red color for printf
RED="\033[0;31m"

# no color for printf
NC="\033[0m"

# change directory to src
cd src

# run uvicorn depends on environment
if [[ $ENVIRONMENT = "DEVELOPMENT" ]]
then
    uvicorn main:app --host=${WEB_UVICORN_HOST}             \
                     --port ${WEB_UVICORN_PORT}             \
                     --ssl-keyfile=${SSL_KEYFILE_PATH}      \
                     --ssl-certfile=${SSL_CERTFILE_PATH}    \
                     --reload                               \
                     --proxy-headers
elif [[ $ENVIRONMENT = "PRODUCTION" ]]
then
    uvicorn main:app --host=${WEB_UVICORN_HOST}             \
                     --port ${WEB_UVICORN_PORT}             \
                     --ssl-keyfile=${SSL_KEYFILE_PATH}      \
                     --ssl-certfile=${SSL_CERTFILE_PATH}    \
                     --workers=${WORKERS}                   \
                     --proxy-headers
else
    printf "${RED}Evironment is not specified.${NC}\n";
fi
