FROM python:3.11-slim

WORKDIR /app

# Install system dependencies (pg_isready lives here)
RUN apt-get update && apt-get install -y postgresql-client

# Copy requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Make wait script executable
RUN chmod +x wait-for-db.sh

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
