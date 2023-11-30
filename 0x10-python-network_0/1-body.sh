#!/usr/bin/env bash
#Only 200 may pass
if [ $(curl -sL -X HEAD -w "%{http_code}" "$1") == '200' ]; then curl -sL "$1"; fi
