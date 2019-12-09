#!/usr/bin/env bash
# shellcheck disable=SC2086
set -Eeuo pipefail

IFS=,

apply() {
    # shellcheck disable=SC1102
    data[${data[(($1 + 3))]}]=$((${data[data[(($1 + 1))]]} $2 ${data[data[(($1 + 2))]]}))
}

read -ra data <<<"${1:?missing required input}"

declare -i i
for ((i=0; data[i] != 99; i+=4)); do
    case ${data[$i]} in
    1) apply $i '+';;
    2) apply $i '*';;
    *) echo "Unknown opcode ${data[$i]}: something went wrong" >&2 && exit 1 ;;
    esac
done

echo "${data[*]}"
