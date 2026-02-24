FROM python:3.11-slim

WORKDIR /app

# Install deps first (cache layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

# Editable install for pytest discovery
RUN pip install -e .

# Test command
CMD ["pytest", "tests/", "-v", "--tb=short"]
