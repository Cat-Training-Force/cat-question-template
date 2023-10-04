#!/bin/sh

echo $GZCTF_FLAG > /chall/secret.txt
unset GZCTF_FLAG

cd /tmp && python /chall/rest-server.py