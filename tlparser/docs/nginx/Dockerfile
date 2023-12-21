# 1 layer
FROM nginx:alpine
LABEL author="kana.suzucki@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 2 layer
RUN apk update && apk add bash curl postgresql-dev gcc g++ python3-dev musl-dev py3-pip

# 3 layer
RUN pip install typing-extensions sphinx sphinx-material

# 4 layer
WORKDIR /code
COPY src ./

# 5 layer
COPY docs/ ./docs

# 6 layer
RUN sphinx-apidoc -o ./docs ./

# 7 layer
RUN sphinx-build -M html ./docs ./docs

CMD [                                   \
    "/bin/sh" ,                         \
    "-c" ,                              \
    "envsubst                           \
    '$SPHINX_PORT'                      \
     < ./docs/nginx/nginx.conf >        \
     /etc/nginx/conf.d/nginx.conf &&    \
     exec nginx -g 'daemon off;'"       \
]

EXPOSE 7777