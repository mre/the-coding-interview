#!/usr/bin/env bash
# shellcheck disable=SC2086
set -Eeuo pipefail

IFS=,

apply() {
    # shellcheck disable=SC1102
    data[${data[(($ip + 3))]}]=$((${data[data[(($ip + 1))]]} $1 ${data[data[(($ip + 2))]]}))
}

read -ra data <<<"$1"

declare -i ip
for ((ip=0; data[ip] != 99; ip+=4)); do
    case ${data[$ip]} in
    1) apply '+';;
    2) apply '*';;
    *) echo "Unknown opcode ${data[$ip]}" >&2 && exit 1 ;;
    esac
done

echo "${data[*]}"
