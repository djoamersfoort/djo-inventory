FROM python:3.12-alpine AS build

COPY requirements.txt /srv/requirements.txt

RUN apk update && \
    apk add mariadb-dev zlib-dev gcc musl-dev

RUN python -m venv /srv/venv && \
    source /srv/venv/bin/activate && \
    pip3 install --no-cache-dir -r /srv/requirements.txt

FROM python:3.12-alpine

RUN apk update && \
    apk add --no-cache nginx mariadb-connector-c

COPY --from=build /srv/venv /srv/venv
COPY inventory /srv/inventory/inventory/
COPY UI/* /srv/ui/
COPY manage.py requirements.txt /srv/inventory/
COPY docker/docker-entrypoint.sh /
COPY docker/nginx.conf /etc/nginx/nginx.conf

WORKDIR /srv
RUN mkdir static logs

# Port to expose
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR /srv/inventory

ENTRYPOINT ["/docker-entrypoint.sh"]
