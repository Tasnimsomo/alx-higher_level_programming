#!/bin/bash
# Send a request to the provided URL silently and display the size of the response body in bytes
curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'
