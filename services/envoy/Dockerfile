FROM envoyproxy/envoy:v1.22-latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            gettext \
            python3-pip \
    ; \
    apt-get clean

WORKDIR /envoy
COPY envoy.yaml /envoy
COPY entrypoint.sh /

RUN chmod 500 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
