FROM postgres:latest

EXPOSE 5432

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            libpq-dev \
            python3-pip \
    ; \
    apt-get clean

RUN pip3 install psycopg2-binary

WORKDIR /postgres
COPY setup.py /postgres
COPY entrypoint.sh /

RUN chmod 500 /postgres/setup.py
RUN chmod 500 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
