#!/bin/bash
#Return Response length
curl -Is "$1" | grep 'Content-Length' | cut -d ' ' -f 2
