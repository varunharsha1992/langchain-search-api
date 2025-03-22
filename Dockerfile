FROM python:3.11-slim

WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Define build arguments
ARG OPENAI_API_KEY
# Set environment variables from build args
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Run the FastAPI app
CMD uvicorn src.main:app --host=0.0.0.0 --port=${PORT:-8000}
