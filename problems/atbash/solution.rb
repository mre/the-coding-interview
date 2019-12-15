#!/usr/bin/env ruby

a='a'.ord
z='z'.ord
ARGV[0].each_char do |c|
  print(c === "\n" ? c : (z - (c.ord - a)).chr)
end
