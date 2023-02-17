#!/bin/zsh

SCRIPTDIR="$(dirname "$(which "$0")")"

if [ -z "$1" ]; then
    echo "Must specify file";
    exit 1;
fi;

SWAPPED_FILE_NAME=$(echo $1 | sed -E 's/(\.[A-Za-z]{3})/ saveswapped\1/')

echo "$1"
echo "$SWAPPED_FILE_NAME"

cp "$1" "$SWAPPED_FILE_NAME"

python $SCRIPTDIR/saveswap.py --no-backup "$SWAPPED_FILE_NAME"