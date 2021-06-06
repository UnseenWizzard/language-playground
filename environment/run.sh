#!/bin/sh
# docker run -it --rm -p 8081:3000 -v $PWD/user_server_a:/files -w /files friendsofgo/killgrave:0.4.1 -config killgrave_config.yaml
cd ./user_server_a && ./run.sh &&
cd .. &&
cd ./user_server_b && ./run.sh