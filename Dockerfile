FROM python:3.7-alpine as base

FROM base as builder

COPY . .

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

FROM builder

VOLUME [ "./data" ]

CMD [ "python", "./src/scheduler.py" ]