# http://www.careercup.com/question?id=12478687

=begin
First greater number in an array. Given a large array of positive
integers, for an arbitrary integer A, we want to know the first integer in
the array which is greater than or equal A . O(logn) solution required
ex [2, 10,5,6,80]
input : 6 output : 10
input :20 output : 80
NOTES/DISCUSSION
Logarithmic algorithms are extremely efficient because they rapidly converge on a solution.
In general, these algorithms succeed because they reduce the size of the problem by about half each time.
=end

def method_12478687(arr, i)
  # Simple first answer
  # Linear or O(n) behavior
  #arr.sort.each { |n| return n if n > i }

  # Logarithmic or O(log n) behavior
  # Divide-and-counquer algorithm
  #high, low = arr.partition { |n| n > i }
  #high.sort!
  #while high.first <= i
  #  high, low = high.partition { |n| n > i }
  #end
  #high.first

  # Sort and select greater in the one iteration
  greater = 0
  arr.each do |n|
    next if n <= i
    if greater == 0 || n < greater
      greater = n
    end
  end
  greater
end
