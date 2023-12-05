#!/bin/bash
# Display on an HTTP response status coode
curl -sw "%{http_code}" -o /dev/null "$1"
