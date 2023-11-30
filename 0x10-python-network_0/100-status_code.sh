#!/bin/bash
#One command
curl -sLw "%{http_code}" -o /dev/null "$1"
