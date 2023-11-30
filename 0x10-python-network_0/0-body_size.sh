#!/usr/bin/env bash
#Return Response length

length=$(curl -Is "$1" | grep 'Content-Length' | cut -d ' ' -f 2)

echo "$length"
