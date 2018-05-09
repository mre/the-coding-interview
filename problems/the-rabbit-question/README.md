The Rabbit Question
===================

I was asked this question a long time ago at one of my first interviews out of college and it has stuck with me
ever since. I personally think it's a great question because it gives you an opportunity, as an interviewer, to 
see how the candidate thinks and also opens up many avenues of discussion.

First, the setup
----------------

There is a rabbit (or other hopping animal you can draw) at the bottom of a set of stairs. The rabbit can hop up 
one step at a time to reach the top, or he can hop up two steps at a time. How many different combinations of hops 
are there for n steps. Write an algorithm to calculate the number of hop combinations for n steps. 

Example - 4 steps  

1-1-1-1 = 4  
2-1-1   = 4  
1-2-1   = 4  
1-1-2   = 4  
2-2     = 4  

So for 4 steps, there are 5 possible different combinations of 1-2 hops to reach the top.

The answer
----------

If you work out the number of possible hops for the first few steps you end up with:

n | hops  
1 | 1  
2 | 2  
3 | 3  
4 | 5  
5 | 8  
6 | 13  

This is the fibonacci sequence (the next number in the sequence is the sum of the two previous numbers). The sequence of 
fibonacci numbers can be expressed like this:

f(n) = f(n-1) + f(n-2)  
f(1) = 1  
f(0) = 0  

In my opinion the most natural way to implement fibonacci is recursively, but it's also possible to implement it iteratively,
as a generator and there's even a closed form expression. I've included the recursive, iterative and generator answers as part
of the solution.

How to ask the question
-----------------------

The important thing about this question isn't that the candidate recognizes the fact that the sequence is fibonacci, but actually
in the follow up questions, which we will discuss later. 

When I ask this question I like to work through the above example with them to make sure they understand the question and then watch 
them work out the answer for other steps. A lot of candidates will recognize the pattern very quickly, but if they don't it's not a 
big deal. Once they either worked out the pattern or given up give them the formula and the method signature:

int fib(int n){ /* your code goes here /* }

This is what you want them to implement.

Regardless of whether they choose to implement the algorithm iteratively or recursively you want them to end up implementing them both.

The follow up questions
-----------------------

 * Is the return type for the function suitable, if not what would be a good alternative?
 * What happens for a large value of n?
 * How many times is the fib function called for n in the recursive implementation?
 * Which algorithm is better, recursive or iterative?
 * How could you optimize the recursive function to make it more performant?
