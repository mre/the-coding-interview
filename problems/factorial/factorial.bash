#!/usr/bin/env bash
set -Eeuo pipefail

loop() {
  declare -i n=$1
  if ((n <= 1)); then
    echo 1
  else
    declare -i acc=1
    while ((n > 1)); do
      ((acc *= n--))
    done
    echo $acc
  fi
}

recursive() {
  declare -i n=$1
  if ((n <= 1)); then
    echo 1
  else
    echo $((n * $(recursive $((n - 1)))))
  fi
}

fail=false
assert() {
  declare -i actual
  declare -i expected=$3
  actual=$("$1" "$2")
  if ((actual != expected)); then
    echo "$1: expected '$expected' got '$actual'" >&2
    fail=true
  fi
}

for f in loop recursive; do
  assert $f 0 1
  assert $f 1 1
  assert $f 2 2
  assert $f 3 6
  assert $f 4 24
  assert $f 5 120
  assert $f 20 2432902008176640000
done

[[ $fail == false ]] || exit 1
