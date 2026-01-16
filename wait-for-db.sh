#!/bin/sh
set -e

host="$1"
shift

until pg_isready -h "$host"; do
  echo "Waiting for Postgres..."
  sleep 2
done

exec "$@"
