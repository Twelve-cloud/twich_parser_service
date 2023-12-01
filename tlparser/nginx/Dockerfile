# 1 layer
FROM nginx:1.25

# 2 layer
RUN rm /etc/nginx/conf.d/default.conf

# 3 layer
COPY ./nginx.conf /nginx.conf

CMD [                                   \
    "/bin/sh" ,                         \
    "-c" ,                              \
    "envsubst                           \
    '$WEB_UVICORN_HOSTNAME $WEB_UVICORN_PORT $WEB_NGINX_PORT'   \
     < /nginx.conf >                    \
     /etc/nginx/conf.d/nginx.conf &&    \
     exec nginx -g 'daemon off;'"       \
]