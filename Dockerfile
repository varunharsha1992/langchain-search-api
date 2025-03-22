FROM python:3.11-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Environment variables will be passed from Heroku
# No need to set them here

# Run the FastAPI app
CMD uvicorn src.main:app --host=0.0.0.0 --port=${PORT:-8000}
