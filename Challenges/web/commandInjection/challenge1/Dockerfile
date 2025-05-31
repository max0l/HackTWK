# Use the official Python 3.8 slim image as the base image
FROM --platform=linux/i386 python:3.10-slim

RUN useradd -m app
RUN apt update && apt upgrade -y && apt install python3-pip -y
# Set the working directory within the container
WORKDIR /commandInjectionLab

# Copy the necessary files and directories into the container
COPY templates/ /commandInjectionLab/templates/
COPY static/ /commandInjectionLab/static/
COPY .env main.py requirements.txt flag.txt /commandInjectionLab/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip install -r requirements.txt

# adjusting environment permissions
RUN chown -R root:root /commandInjectionLab
RUN chmod -R 555 /commandInjectionLab
RUN chown -R app:app /commandInjectionLab/templates
RUN chmod -R 777 /commandInjectionLab/templates
RUN chown -R app:app /commandInjectionLab/static
RUN chmod -R 777 /commandInjectionLab/static
RUN chmod 444 /commandInjectionLab/flag.txt
RUN chmod 444 /commandInjectionLab/.env


RUN chown -R root:root /commandInjectionLab
RUN chmod -R 555 /commandInjectionLab

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application using Gunicorn
USER app
CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000", "-w", "4"]