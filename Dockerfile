FROM python:3-alpine
COPY parse.py /
WORKDIR /
RUN apk --no-cache add curl  
ENTRYPOINT /parse.py
