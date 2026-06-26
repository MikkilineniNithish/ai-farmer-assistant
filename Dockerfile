# Start with Python 3.11
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for faster builds)
COPY requirements.txt .

# Install all libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Tell Docker which port to use
EXPOSE 10000

# Start the app
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "main:app"]