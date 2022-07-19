FROM mongo:latest

EXPOSE 27017
WORKDIR /mongoDB
COPY entrypoint.sh /

RUN chmod 500 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
