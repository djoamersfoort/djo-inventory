FROM python:3.12-slim

COPY inventory /srv/inventory/inventory/
COPY UI/* /srv/ui/
COPY manage.py requirements.txt /srv/inventory/
COPY docker/docker-entrypoint.sh /

RUN apt-get -y update && apt-get -y install nginx libmariadb-dev && apt-get clean && \
    pip3 install --no-cache-dir -r /srv/inventory/requirements.txt

COPY docker/nginx.conf /etc/nginx/nginx.conf

WORKDIR /srv
RUN mkdir static logs

# Port to expose
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR /srv/inventory

ENTRYPOINT ["/docker-entrypoint.sh"]
