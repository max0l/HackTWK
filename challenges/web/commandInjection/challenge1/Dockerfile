# Use the official Python 3.8 slim image as the base image
FROM python:3.13

# Set the working directory within the container
WORKDIR /commandInjectionLab

# Copy the necessary files and directories into the container
COPY templates/ /commandInjectionLab/templates/
COPY static/ /commandInjectionLab/static/
COPY .env main.py requirements.txt flag.txt /commandInjectionLab/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN chown -R root:root /commandInjectionLab
RUN chmod -R 555 /commandInjectionLab

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]