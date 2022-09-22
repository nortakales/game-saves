#!/bin/bash

# Just trims the known amount of bytes for a dsv footer
head -c -122 "$1" > "$2"
tail -c 122 "$1" > "$1.footer"