#!/bin/bash
#What can I do
curl -isL -X OPTIONS "$1" | grep "Allow" | cut -d "" -f2-
