#!/usr/bin/env dart

import 'dart:io';
import 'dart:math';

class Pair {
  final int first;
  final int second;

  Pair(this.first, this.second);

  @override
  String toString() => "($first, $second)";
}

void main(List<String> arguments) {
  var input = arguments[0].split(',').map(int.parse).toList();
  int k = input.removeAt(0);
  var seen = <int>{};
  var pairs = <Pair>[];

  input.forEach((n) {
    int x = k - n;
    if (x != n) {
      if (seen.contains(x)) {
        pairs.add(new Pair(min(x, n), max(x, n)));
      } else {
        seen.add(n);
      }
    }
  });

  stdout.write('[');
  for (int i = 0; i < pairs.length; i++) {
    if (i != 0) {
      stdout.write(', ');
    }
    stdout.write(pairs[i]);
  }
  stdout.write(']');
}
