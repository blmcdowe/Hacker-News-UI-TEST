# This is Docker is intended to test and validate docker_test0_test.py file
# Use official Python slim image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your project files
COPY . .

# Install Playwright browsers and dependencies
RUN playwright install --with-deps

# Default command to run tests

CMD ["pytest", "-s", "automated-ui-sorting-check.py"]
