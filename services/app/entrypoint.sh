#!/bin/sh
set -e

uwsgi --ini uwsgi.ini

exec "$@"
