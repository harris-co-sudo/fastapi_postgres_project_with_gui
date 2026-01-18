#!/bin/sh
# wait-for-db.sh

echo "Waiting for Postgres database to be ready..."

# Loop until Postgres is ready
while ! pg_isready -h db -p 5432 -U postgres; do
  sleep 2
done

echo "Database is ready! Starting FastAPI..."

# Start FastAPI
exec uvicorn app.main:app --host 0.0.0.0 --port 8000

