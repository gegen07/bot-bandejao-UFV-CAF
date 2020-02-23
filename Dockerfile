FROM python:3.7-alpine as base

FROM base as builder

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM base

COPY src/ src

COPY ./data/ data/
VOLUME [ "/data" ]


CMD [ "python", "./src/scheduler.py" ]