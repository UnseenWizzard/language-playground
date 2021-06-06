#!/bin/sh
java -jar ../wiremock-jre8-standalone-2.28.0.jar --bind-address 0.0.0.0 --port 8081 --local-response-templating &