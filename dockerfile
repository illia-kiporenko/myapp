# Base image
FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy app and test code
COPY app.py .
COPY test_app.py .

# Install dependencies
RUN pip install flask pytest

# Default command
CMD ["pytest"]
