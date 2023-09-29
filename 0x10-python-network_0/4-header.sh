#!/bin/bash
# This will take in a url as an argument sends a GET request and disiplays the body
curl -s "$1" -H "X-School-User-Id: 98"
