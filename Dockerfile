FROM python:3.11-slim

WORKDIR /app

# Install Postgres client for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Make wait-for-db.sh executable
RUN chmod +x wait-for-db.sh

# Run the wait script to start FastAPI after DB is ready
CMD ["./wait-for-db.sh"]
