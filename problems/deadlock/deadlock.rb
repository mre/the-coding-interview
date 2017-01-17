require 'thread'
mutex1 = Mutex.new
mutex2 = Mutex.new

t1 = Thread.new do
   loop do
      puts "Thread 1: Aquiring mutex 1"
      mutex1.synchronize do
        puts "Thread 1: Aquiring mutex 2"
        mutex2.synchronize do
        end
      end
    end
end
t2 = Thread.new do
   loop do
      puts "Thread 2: Aquiring mutex 2"
      mutex2.synchronize do
        puts "Thread 2: Aquiring mutex 1"
        mutex1.synchronize do
        end
      end
    end
end
