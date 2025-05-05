# Use an official Python runtime as a base image
FROM --platform=linux/i386 python:3.10-slim

RUN useradd -m app
RUN apt-get update && apt upgrade && apt install python3-pip -y

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files and directories into the container
COPY templates/ /app/templates/
COPY static/ /app/static/
COPY .env main.py requirements.txt flag.txt /app/

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN chown -R root:root /app
RUN chmod -R 555 /app
RUN chmod 444 /app/flag.txt
RUN chmod 444 /app/requirements.txt
RUN chmod 444 /app/.env


# Expose the port the app runs on
EXPOSE 5000

# Run the app
CMD ["python", "main.py"]
