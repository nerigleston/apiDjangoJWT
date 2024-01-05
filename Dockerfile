FROM ubuntu:18.04

ENV SECRET_KEY='django-insecure-_q34gykfpgt7x%t6y05&cn4=#7t75ja8*0rdwu&#nu$n_=en0-'

WORKDIR /code

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    zlib1g-dev \
    libjpeg-dev

COPY requirements.txt /code

COPY . /code

RUN pip3 install --no-cache-dir -r requirements.txt

CMD python3 manage.py runserver 8000
