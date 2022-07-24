FROM postgres:latest

EXPOSE 5432

WORKDIR /postgres
COPY entrypoint.sh /

RUN chmod 500 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
