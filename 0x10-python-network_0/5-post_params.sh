#!/bin/bash
# HTTP request with some parameters
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
