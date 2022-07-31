FROM python:3.10-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            gcc  \
            libc6-dev \
            libpq-dev \
    ; \
    apt-get clean

EXPOSE 6200

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
RUN chmod 500 /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
