#!/usr/bin/env bash
set -Eeuo pipefail

declare -i sum=0
while read -r n; do
    while ((n > 0)); do
        n=$((n / 3 - 2))
        n=$((n > 0 ? n : 0))
        ((sum += n))
    done
done <<<"$1"
echo $sum
