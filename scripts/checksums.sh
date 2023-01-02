#!/bin/zsh

# zsh is important for the current expansion to work
# for bash, you would need to do: shopt -s globstar
# This helped: https://thevaluable.dev/zsh-expansion-guide-example/

SCRIPTDIR="$(dirname "$(which "$0")")"

touch EMPTY_FILE.txt

declare -A CHECKSUMS

for FILE in ./**/*(.)
do
    CHECKSUM=$(md5sum "$FILE" | cut -d' ' -f1)
    # echo "$CHECKSUM $FILE"
    ALLOW_LIST_RESULT=$(grep $FILE $SCRIPTDIR/checksums-allow-list.txt)
    if [[ ! -z ${CHECKSUMS[$CHECKSUM]} && -z $ALLOW_LIST_RESULT ]]; then
        echo "\e[0;0m$FILE\e[0;37m matches \e[0;0m${CHECKSUMS[$CHECKSUM]}"
        echo "\e[0;35m    $CHECKSUM\e[0;0m"
    else
        CHECKSUMS[$CHECKSUM]=$FILE
    fi
done

rm EMPTY_FILE.txt

# echo "${CHECKSUMS[@]}"
# echo ${CHECKSUMS['sdf']}