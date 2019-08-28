FROM python:3.7-alpine3.10

# Install ca-certificates so that HTTPS works consistently
RUN apk update && \
	apk add --no-cache git

WORKDIR /msrdemo

COPY requirements.txt /msrdemo/requirements.txt

RUN pip install --trusted-host pypi.python.org -r requirements.txt

COPY . /msrdemo

