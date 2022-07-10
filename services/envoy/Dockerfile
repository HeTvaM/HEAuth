FROM envoyproxy/envoy:v1.22-latest

RUN apt-get update && \
    apt-get install gettext -y && \
    apt-get install python3-pip -y && \
    apt-get clean

WORKDIR /envoy
COPY envoy.yaml /envoy
COPY entrypoint.sh /

RUN chmod 500 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
