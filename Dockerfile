FROM python:3.6-alpine

# Set the file maintainer (your name - the file's author)
MAINTAINER Ronald Moesbergen

COPY inventory /srv/inventory/inventory/
COPY UI/* /srv/ui/
COPY manage.py requirements.txt /srv/inventory/
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY docker/docker-entrypoint.sh /

RUN apk update && \
    apk add nginx mariadb-dev zlib-dev gcc musl-dev jpeg-dev freetype-dev && \
    pip3 install --no-cache-dir -r /srv/inventory/requirements.txt && \
    rm -f /srv/inventory/inventory/settings.py && \
    apk del gcc musl-dev

WORKDIR /srv
RUN mkdir static logs /run/nginx

# Port to expose
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR /srv/inventory

ENTRYPOINT ["/docker-entrypoint.sh"]
