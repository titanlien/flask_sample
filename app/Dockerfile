FROM python:2.7.11
MAINTAINER titan lien <titan.lien@gmail.com>

RUN apt-get -qy autoremove
ADD requirements.txt /tmp
RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

EXPOSE 5000
COPY src /app
CMD uwsgi --ini /app/wsgi.ini
