# Use a base Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files
COPY requirements.txt .env ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 8080
EXPOSE ${PORT:-8080}

# Default command to run the application
CMD ["sh", "-c", "uvicorn app.main:app --host ${HOST:-0.0.0.0} --port ${PORT:-8080}"]