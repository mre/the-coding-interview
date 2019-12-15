#!/usr/bin/env bash
set -Eeuo pipefail

declare -i a z
a=$(printf %d \'a)
z=$(printf %d \'z)
for ((i = 0; i < ${#1}; i++)); do
    if [[ "${1:$i:1}" == $'\n' ]]; then
        echo
    else
        # shellcheck disable=SC2059
        printf "\x$(printf %x $((z - ($(printf %d "'${1:$i:1}") - a))))"
    fi
done
