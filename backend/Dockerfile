FROM python:3.10.0
RUN mkdir /usr/src/app/
COPY . /usr/src/app/
WORKDIR /usr/src/app/
EXPOSE 5000
RUN apt update \
    && apt install libpq-dev gcc \
    && pip install -r requirements.txt