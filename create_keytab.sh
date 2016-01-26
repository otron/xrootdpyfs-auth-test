#!/bin/bash

principal="$2"
output="$1"
ktutil -k $1 add -p principal -e arcfour-hmac-md5 -V 1
