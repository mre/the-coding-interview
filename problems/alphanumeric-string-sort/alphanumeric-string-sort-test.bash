#!/usr/bin/env bash
set -Eeuo pipefail

fail=false
assert() {
  if [[ "$(./alphanumeric-string-sort.bash "$1")" != "$2" ]]; then
    echo "expected '$2' got '$1'" >&2
    fail=true
  fi
}

assert 'Sorting0123456789' 'ginortS0246813579'
assert 'foobar1237348421' 'abfoor2244811337'
assert '90856123456789' '02466881355799'

if [[ $fail == true ]]; then
  exit 1
fi
