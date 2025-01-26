FROM gcr.io/distroless/java21

WORKDIR /app

COPY out/artifacts/ctf_jar/ctf.jar /app/app.jar

EXPOSE 4000

CMD ["app.jar"]