#!/bin/bash

# Just trims the known amount of bytes for a dsv footer
# https://github.com/jojojo8359/DeSmuMESaveConverter/blob/master/main.py
# https://github.com/j-tai/dsv2sav/blob/master/dsv2sav.py
head -c -122 "$1" > "$2"
tail -c 122 "$1" > "$1.footer"