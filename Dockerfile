FROM python:3-alpine
COPY parse.py /
WORKDIR /
RUN /parse.py A
