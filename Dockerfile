FROM openjdk:21-jdk-slim

WORKDIR /app

COPY out/artifacts/ctf_jar/ctf.jar /app/app.jar

EXPOSE 4000

CMD ["java", "-jar", "/app/app.jar"]