#!/usr/bin/env bash
set -Eeuo pipefail

parent=${1%$'\n'*}
child=${1#*$'\n'}

parent_len=${#parent}
child_len=${#child}

sum() {
    declare -i result=0
    while read -rn1 c; do
        ((result += $(printf '%d' "'$c")))
    done <<<"$1"
    echo $result
}

if ((parent_len == child_len)); then
    echo $(($(sum "$parent") == $(sum "$child")))
else
    readonly child_sum=$(sum "$child")
    declare -i result=0
    declare -i start=0

    while (((start + child_len) < parent_len)); do
        if (($(sum "${parent:$start:$child_len}") == child_sum)); then
            ((++result))
        fi
        ((++start))
    done

    echo $result
fi
