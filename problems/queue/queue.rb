#!/usr/bin/env ruby

class Queue
    def initialize
        @queue = []
    end 
    
    def add(val)
        @queue << val
    end

    def remove
        @queue.shift
    end
end

q = Queue.new
q.add(1)
q.add(2)
q.add(3)
puts q.remove()
puts q.remove()
puts q.remove()
puts q.remove()
