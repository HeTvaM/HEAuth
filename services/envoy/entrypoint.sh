#!/bin/sh
set -e

cat /envoy/envoy.yaml | envsubst "$(printf '${%s} ' $(env | cut -d'=' -f1))" > envoy.yaml

envoy -c envoy.yaml
