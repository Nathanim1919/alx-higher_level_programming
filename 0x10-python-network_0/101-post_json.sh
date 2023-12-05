#!/bin/bash
# Send a JSON file to a URLand display the body of the response
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
