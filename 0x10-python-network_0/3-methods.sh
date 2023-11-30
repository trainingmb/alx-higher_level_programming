#!/bin/bash
#What can I do
curl -i -L -X OPTIONS "$1" | grep "Allow" | cut -d "" -f 2
