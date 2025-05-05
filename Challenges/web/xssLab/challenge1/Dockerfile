# Use an official Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /challenge1

# Copy project files
COPY . .

# Install Flask (and other requirements if needed)
RUN pip install -r requirements.txt

# Expose port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]