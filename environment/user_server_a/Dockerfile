FROM openjdk:8-alpine
RUN mkdir wiremock
WORKDIR wiremock
RUN wget https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-jre8-standalone/2.28.0/wiremock-jre8-standalone-2.28.0.jar
COPY mappings mappings
CMD ["java", "-jar", "wiremock-jre8-standalone-2.28.0.jar", "--local-response-templating"]