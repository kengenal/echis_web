# Python build stage
FROM python:3.8.6-alpine3.12

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    gcc \
    libc-dev \
    libffi-dev \
    python3-dev \
    musl-dev \
    mariadb-dev


RUN mkdir -p /app
RUN adduser -Ds /bin/ash flask
RUN chown -R flask:flask /app
RUN chmod 755 /app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN pip install -U pip
RUN pip install poetry

COPY ./pyproject.toml pyproject.toml

RUN poetry config virtualenvs.create false \
    && poetry install

COPY --chown=flask:flask ./build/python/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

USER flask

WORKDIR /app

EXPOSE 5000

ENTRYPOINT ["sh", "/entrypoint"]
