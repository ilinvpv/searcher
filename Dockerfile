FROM python:3.7-alpine
RUN addgroup -g 1000 -S alpine && adduser -u 1000 -S alpine -G alpine

RUN apk update && \
    apk add gcc postgresql-dev graphviz-dev python3-dev musl-dev imagemagick-dev libcap-dev libffi-dev \
    pcre-dev zlib-dev curl-dev coreutils sudo py3-psutil py3-dateutil py3-tz \
    py3-cparser alpine-sdk linux-headers bash libc6-compat gcompat && \
    pip install setuptools --upgrade

WORKDIR /home/alpine

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt && pip install --no-cache-dir uwsgi

ENV PYTHONPATH "${PYTHONPATH}:/home/alpine"
USER alpine
COPY ./searcher ./searcher
