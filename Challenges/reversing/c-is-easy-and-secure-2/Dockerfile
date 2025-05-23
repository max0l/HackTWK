FROM --platform=linux/amd64 ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential socat

COPY main.c /app
COPY Makefile /app

RUN make private.elf

RUN rm /app/main.c && rm /app/Makefile

RUN chmod +x /app

RUN chown root:root /app/*

RUN chmod -R o-w /app/*

RUN useradd app

USER app

ENTRYPOINT socat TCP-LISTEN:1337,reuseaddr,fork EXEC:/app/private.elf