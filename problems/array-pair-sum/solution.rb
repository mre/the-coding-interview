#!/usr/bin/env ruby

input = ARGV.first.split(',').map(&:to_i)
target, arr = input[0], input[1..-1]

def find_pair(target, arr)
    map = {}
    pairs = []
    arr.each do |n|
        x = target - n
        if map[x]  && x != n 
            pairs << [[x, n].min, [x, n].max]
        else
            map[n] = true
        end
    end

    pairs
end

puts find_pair(target, arr).inspect
