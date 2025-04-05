FROM --platform=linux/i386 python:3.10-slim

RUN useradd -m app
RUN apt-get update && apt-get install -y unzip chromium

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true
ENV PYPPETEER_HOME '/tmp/'

WORKDIR /app
COPY . .

RUN chown -R root:root /app
RUN chmod -R 555 /app
RUN mkdir /app/uploads
RUN chown -R app:app /app/uploads
RUN chmod -R 777 /app/uploads
RUN chmod 111 /app/flag

RUN pip3 install -r requirements.txt

USER app
ENTRYPOINT ["python3", "app.py"]
