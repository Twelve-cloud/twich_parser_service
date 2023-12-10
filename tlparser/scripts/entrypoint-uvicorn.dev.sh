#! /bin/bash
uvicorn main:app --host=${WEB_UVICORN_HOST} --port ${WEB_UVICORN_PORT} --ssl-keyfile=./certs/cert.key --ssl-certfile=./certs/cert.crt