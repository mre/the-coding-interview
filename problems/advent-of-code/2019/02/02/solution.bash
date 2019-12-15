#!/usr/bin/env bash
# shellcheck disable=SC2086
set -Eeuo pipefail

IFS=,

apply() {
    # shellcheck disable=SC1102
    data[${data[(($1 + 3))]}]=$((${data[data[(($1 + 1))]]} $2 ${data[data[(($1 + 2))]]}))
}

int_computer() {
    declare -i ip
    for ((ip=0; data[ip] != 99; ip+=4)); do
        case ${data[$ip]} in
        1) apply $ip '+';;
        2) apply $ip '*';;
        *) echo "Unknown opcode ${data[$ip]}" >&2 && exit 1 ;;
        esac
    done
}

read -ra input <<<"$1"

declare -i noun verb
for noun in {0..99}; do
    for verb in {0..99}; do
        data=("${input[@]}")
        data[1]=$noun
        data[2]=$verb
        int_computer
        if ((data[0] == 19690720)); then
            echo $((100 * noun + verb))
            exit 0
        fi
    done
done
exit 1
