#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ]; then
    echo "Must specify two files";
    exit 1;
fi;

xxd "$1" > 1.hex
xxd "$2" > 2.hex
git diff --no-index 1.hex 2.hex
rm 1.hex
rm 2.hex