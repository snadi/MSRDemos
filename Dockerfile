FROM python:3.7-slim

RUN apt-get update && \
	apt-get install git -y

WORKDIR /msrdemo

COPY requirements.txt /msrdemo/requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /msrdemo
