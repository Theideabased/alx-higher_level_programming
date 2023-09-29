#!/bin/bash
# this will take a url and send a request to that url
curl -sI "$1" | awk '/Content-Length/{print $2}'
