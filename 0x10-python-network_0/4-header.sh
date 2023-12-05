#!/bin/bash
# Display HTTP response body of a request made with an header
curl -sH "X-School-User-Id: 98" "$1"
