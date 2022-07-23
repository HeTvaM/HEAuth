FROM postgres:latest
FROM python:3.10

EXPOSE 5432

WORKDIR /postgres
COPY . /postgresDB
RUN chmod 500 /app/entrypoint.sh

ENTRYPOINT ["/postgresDB/entrypoint.sh"]

