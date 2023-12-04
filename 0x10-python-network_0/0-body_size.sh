#!/bin/bash
# Use curl to fetch the URL and display the size of the body in bytes
curl -sI "$1" | grep "Content-Length" | awk '{print $2}' | tr -d '\r'
