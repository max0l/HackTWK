# Use the official Python 3.8 slim image as the base image
FROM python:3.13

# Set the working directory within the container
WORKDIR /commandInjectionLab2

# Copy the necessary files and directories into the container
COPY templates/ /commandInjectionLab2/templates/
COPY static/ /commandInjectionLab2/static/
COPY .env main.py requirements.txt flag.txt /commandInjectionLab2/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN chown -R root:root /commandInjectionLab2
RUN chmod -R 555 /commandInjectionLab2

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]