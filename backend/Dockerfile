FROM python:3.10.0
COPY ./requirements.txt /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN apt update \
    && apt install libpq-dev gcc \
    && pip install -r requirements.txt