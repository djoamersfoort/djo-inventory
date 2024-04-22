FROM python:3.11-slim

# Set the file maintainer (your name - the file's author)
MAINTAINER Ronald Moesbergen

COPY inventory /srv/inventory/inventory/
COPY UI/* /srv/ui/
COPY manage.py requirements.txt /srv/inventory/
COPY docker/docker-entrypoint.sh /

RUN apt-get -y update && apt-get -y install build-essential pkg-config nginx libmariadb-dev && apt-get clean && \
    pip3 install --no-cache-dir -r /srv/inventory/requirements.txt && \
    apt-get -y purge build-essential pkg-config && apt-get -y autoremove --purge build-essential

COPY docker/nginx.conf /etc/nginx/nginx.conf

WORKDIR /srv
RUN mkdir static logs

# Port to expose
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR /srv/inventory

ENTRYPOINT ["/docker-entrypoint.sh"]
