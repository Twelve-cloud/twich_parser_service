#! /bin/bash
uvicorn main:app --host=${WEB_UVICORN_HOST}             \
                 --port ${WEB_UVICORN_PORT}             \
                 --ssl-keyfile=/etc/ssl/certs/cert.key  \
                 --ssl-certfile=/etc/ssl/certs/cert.crt \
                 --workers=8                            \
                 --proxy-headers                        \
