#!/usr/bin/env ruby

def sub_strings(str)
  sub_strs = str.split('')

  str.size.times do |i|
    for j in (i+1...str.size)
      sub_strs << str[i..j]
    end
  end

  sub_strs
end

puts sub_strings('abc').inspect