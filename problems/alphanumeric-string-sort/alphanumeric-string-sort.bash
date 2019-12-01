#!/usr/bin/env bash
set -Eeuo pipefail

declare -a lower upper even odd

while read -rn1 c; do
  if [[ "$c" =~ [a-z] ]]; then
    lower+=("$c")
  elif [[ "$c" =~ [A-Z] ]]; then
    upper+=("$c")
  elif [[ ! "$c" =~ [0-9] ]]; then
    if [[ "$c" != '' ]]; then
      echo "String must be alphanumeric, got: '$1'" >&2
      exit 64
    fi
  elif ((c % 2 == 0)); then
    even+=("$c")
  else
    odd+=("$c")
  fi
done <<<"$1"

print() { printf '%s\n' "$@" | sort | xargs -r printf '%s'; }
print "${lower[@]}"
print "${upper[@]}"
print "${even[@]}"
print "${odd[@]}"
echo
