#!/usr/bin/env bash
set -Eeuo pipefail

IFS=, read -ra input <<<"$1"
declare -i k=${input[0]}
declare -A seen=()
declare -a pairs=()

for n in "${input[@]:1}"; do
    declare -i x=$((k - n))
    if ((x != n)); then
        if [[ -n "${seen[$x]:-}" ]]; then
            pairs+=("($((x < n ? x : n)), $((x > n ? x : n)))")
        else
            seen[$n]=1
        fi
    fi
done

printf '['
declare -i i=0
for pair in "${pairs[@]}"; do
    if ((i++ != 0)); then
        printf ', '
    fi
    printf '%s' "$pair"
done
printf ']\n'
