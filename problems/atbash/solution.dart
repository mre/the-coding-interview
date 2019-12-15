#!/usr/bin/env dart

import 'dart:io';

void main(List<String> arguments) {
  int a = 'a'.codeUnitAt(0);
  int z = 'z'.codeUnitAt(0);
  int lf = '\n'.codeUnitAt(0);
  arguments[0].runes.forEach((int c) {
    stdout.write(String.fromCharCode(c == lf ? c : z - (c - a)));
  });
}
