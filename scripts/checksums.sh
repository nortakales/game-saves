#!/bin/zsh

# zsh is important for the current expansion to work
# for bash, you would need to do: shopt -s globstar
# This helped: https://thevaluable.dev/zsh-expansion-guide-example/

declare -A CHECKSUMS

for FILE in ./**/*(.)
do
    CHECKSUM=$(md5sum "$FILE" | cut -d' ' -f1)
    # echo "$CHECKSUM $FILE"
    if [[ ! -z ${CHECKSUMS[$CHECKSUM]} ]]; then
        echo $FILE " matches " ${CHECKSUMS[$CHECKSUM]}
    else
        CHECKSUMS[$CHECKSUM]=$FILE
    fi
done

# echo "${CHECKSUMS[@]}"
# echo ${CHECKSUMS['sdf']}