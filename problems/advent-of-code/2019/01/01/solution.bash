#!/usr/bin/env bash
set -Eeuo pipefail

declare -i sum=0
while read -r n; do
    ((sum += n / 3 - 2))
done <<<"$1"
echo $sum
