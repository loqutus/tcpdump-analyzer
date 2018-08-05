FROM python:3-alpine
COPY parse.py /
WORKDIR /
ENTRYPOINT /parse.py
