#!/bin/bash

NEW_FILE=`echo "$1" | sed s/\.sav$/\.dsv/`

if [[ -f "$NEW_FILE" ]]; then
    echo "$NEW_FILE already exists, exiting"
    exit 1
fi

# All values below are little endian

# |<--Snip above here to create a raw sav by excluding this DeSmuME savedata footer:
START_FOOTER=\\x7c\\x3c\\x2d\\x2d\\x53\\x6e\\x69\\x70\\x20\\x61\\x62\\x6f\\x76\\x65\\x20\\x68\\x65\\x72\\x65\\x20\\x74\\x6f\\x20\\x63\\x72\\x65\\x61\\x74\\x65\\x20\\x61\\x20\\x72\\x61\\x77\\x20\\x73\\x61\\x76\\x20\\x62\\x79\\x20\\x65\\x78\\x63\\x6c\\x75\\x64\\x69\\x6e\\x67\\x20\\x74\\x68\\x69\\x73\\x20\\x44\\x65\\x53\\x6d\\x75\\x4d\\x45\\x20\\x73\\x61\\x76\\x65\\x64\\x61\\x74\\x61\\x20\\x66\\x6f\\x6f\\x74\\x65\\x72\\x3a
# |-DESMUME SAVE-|
END_FOOTER=\\x7c\\x2d\\x44\\x45\\x53\\x4d\\x55\\x4d\\x45\\x20\\x53\\x41\\x56\\x45\\x2d\\x7c

echo "New file will be $NEW_FILE"
SAV_SIZE=`wc -c "$1" | cut -d' ' -f1`
echo "Detected sav size: $SAV_SIZE"
# Converts to hex padded to 8 bytes, converts to little endian, trims the new line, adds the \\x
UINT32_LE_SAV_SIZE=`printf "%08x\n" $SAV_SIZE | tac -rs .. | tr -d '\n' | sed -e "s/\(..\)/\\\\\\\\x\1/g"`
echo "Size as LE uint32: $UINT32_LE_SAV_SIZE"

WRITTEN_SIZE=$UINT32_LE_SAV_SIZE # Set to sav size in Drastic
PADDED_SIZE=$UINT32_LE_SAV_SIZE # Set to sav size in Drastic
SAVE_TYPE=\\x00\\x00\\x00\\x00 # Might not be used by Desmume, always 0 from Drastic
ADDRESS_SIZE=\\x01\\x00\\x00\\x00 # 1, 2 or 3 - default to 1 and adjust below
SIZE_PARAMETER=$UINT32_LE_SAV_SIZE # Set to sav size in Drastic
VERSION=\\x00\\x00\\x00\\x00 # Always 0

if (($SAV_SIZE > 512)); then
    ADDRESS_SIZE=\\x02\\x00\\x00\\x00
fi
if (($SAV_SIZE > 65536)); then
    ADDRESS_SIZE=\\x03\\x00\\x00\\x00
fi
echo "Address size: $ADDRESS_SIZE"

FULL_FOOTER=$START_FOOTER$WRITTEN_SIZE$PADDED_SIZE$SAVE_TYPE$ADDRESS_SIZE$SIZE_PARAMETER$VERSION$END_FOOTER

echo "Full footer:"
echo -n -e $FULL_FOOTER | xxd

read -r -p 'Do you want to continue? [y/n] ' RESPONSE

case "$RESPONSE" in
    [yY][eE][sS]|[yY])
        # Nothing, anything else will quit
        ;;
    *)
        echo 'Exiting...'
        exit 0
        ;;
esac

# Copy the raw sav data first
cat "$1" > "$NEW_FILE"
echo -n -e $FULL_FOOTER >> "$NEW_FILE"

