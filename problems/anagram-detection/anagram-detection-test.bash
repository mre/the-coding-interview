#!/usr/bin/env bash
set -Eeuo pipefail

fail=false
assert() {
  if [[ "$(./anagram-detection.bash -c "$1" "$2")" != "$3" ]]; then
    echo "expected '$2' got '$1'" >&2
    fail=true
  fi
}

assert 'AdnBndAndBdaBn' 'dAn' 4
assert 'AbrAcadAbRa' 'cAda' 2

if [[ $fail == true ]]; then
  exit 1
fi
