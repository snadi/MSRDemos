FROM python:rc-alpine3.10

# Install ca-certificates so that HTTPS works consistently
RUN apk update && \
	apk add --no-cache git

WORKDIR /msrdemo

COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt
