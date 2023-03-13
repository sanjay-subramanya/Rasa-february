FROM python:3.8 AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

COPY l2-banking.py ./
COPY l2-hospitality.py ./
COPY l2-travel.py ./
COPY trans.py ./

EXPOSE 5000
EXPOSE 6000
EXPOSE 7000
EXPOSE 4000

RUN pip install flask
RUN pip install googletrans==3.1.0a0
