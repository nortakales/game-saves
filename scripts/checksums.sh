#!/bin/zsh

# zsh is important for the current expansion to work
# for bash, you would need to do: shopt -s globstar
# This helped: https://thevaluable.dev/zsh-expansion-guide-example/

SCRIPTDIR="$(dirname "$(which "$0")")"

declare -A CHECKSUMS

# Store checksum for empty file first
CHECKSUMS[d41d8cd98f00b204e9800998ecf8427e]=EMPTY

for FILE in ./**/*(.)
do
    CHECKSUM=$(md5sum "$FILE" | cut -d' ' -f1)
    # echo "$CHECKSUM $FILE"
    ALLOW_LIST_RESULT=$(grep "$FILE" $SCRIPTDIR/checksums-allow-list.txt)
    # If checksum already exists, and file is not allowlisted
    if [[ ! -z ${CHECKSUMS[$CHECKSUM]} && -z $ALLOW_LIST_RESULT ]]; then
        echo "\e[0;0m$FILE\e[0;37m matches \e[0;0m${CHECKSUMS[$CHECKSUM]}"
        echo "\e[0;35m    $CHECKSUM\e[0;0m"
        # else if the checksum does not exist
    elif [[ -z ${CHECKSUMS[$CHECKSUM]} ]]; then
        CHECKSUMS[$CHECKSUM]=$FILE
    fi
done

# echo "${CHECKSUMS[@]}"
# echo ${CHECKSUMS['sdf']}