# http://www.careercup.com/question?id=12590665

=begin
Write function that takes two integers m and n respectively.
The function should flip the nth bit of m, counting from the LSB and return the resulting value.
By flip, the interviewer meant change 0 to 1 and 1 to 0. For instance, if you were passed in 8 and 3. 
Convert 8 to binary and you have 1000, now we flip the 3rd bit and we have 1100,
then we convert this back to decimal(which would be 12)and return the answer.
NOTES/DISCUSSION

http://en.wikipedia.org/wiki/Least_significant_bit

http://ruby-doc.org/core-1.9.3/Fixnum.html
fix[n] → 0, 1 click to toggle source
Bit Reference—Returns the nth bit in the binary representation of fix, where fix is the least significant bit.

You can convert decimal to binary directly by using to_s(2) method.
>>> puts 5454.to_s(2)
=> 1010101001110
>> 8.to_s(2)
=> "1000"

Ruby Bitwise Operators
http://www.tutorialspoint.com/ruby/ruby_operators.htm
=end

def method_12590665(m, n)
  m ^ (1 << n - 1)
end
