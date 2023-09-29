#!/bin/bash
# This will take a url and displays all HTTP  methods the server will accept
curl -sI "$1" | grep -i "Allow" | awk -F ": " '{ print $2 }'
