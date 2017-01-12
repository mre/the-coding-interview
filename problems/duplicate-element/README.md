https://www.quora.com/What-are-the-best-programming-interview-questions-youve-ever-asked-or-been-asked

From my experience, the best programming questions are the ones that have multiple approaches with different trade-offs. Observing someone tackle the same problem under different constraints can teach you a lot about the person's attitude and abilities. I'll give a concrete example, and then explain why I think it's a great question.


Problem**: Let's say you have a list of N+1 integers between 1 and N. You know there's at least one duplicate, but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2. Print out a number that appears in the list more than once. (That is, in the first example, you can print '1' or '3' -- you don't have to print both.)

[Pause here if you want to think about the problem because I'm about to give away the solution.]

Here's an idealized conversation:

Interviewer: [states problem]

Candidate: Well, I guess the most obvious approach is to compare every number in the list to every other number until you find a duplicate.

Interviewer: That's a good start. What are the space and time complexities of that solution?

Candidate: O(n^2) time and O(1) space.

Interviewer: Great. Okay, well let's say the list is pretty big, so you need something that's faster than O(n^2).

Candidate: Hm, I guess I could iterate through the list and use a hash to keep track of the values I've seen so far. Once I encounter a number that's already in the hash, I am done.

Interviewer: That's a good idea, but does it need to be a hash given that all of the inputs are integers between 1 and N?

Candidate: Ah, I guess I could just use a boolean array and use the integer values as indices.

Interviewer: What are the space and time complexities of that solution?

Candidate: O(n) time to iterate through the list and O(n) space for the array/hash.

Interviewer: Very good. Okay, let's say the list of numbers is quite large, so you'd like to avoid creating a copy of it. Maybe you have 8GB of RAM, and the list takes up 6GB.

Candidate: Well, I could sort the numbers and compare adjacent pairs. That would take O(n*log n) time and O(1) space if I use an in-place sort like mergesort.

Interviewer: Excellent. Let's throw in one final constraint: what if you want something faster than O(n^2) and you can't afford to use a lot of extra space, but you also can't manipulate the original list. For example, maybe the list is on a read-only CD.

(Almost every candidate needs a hint or two at this point..)

Candidate: I think I can binary search for a duplicated number. For example, I go through the list and count the number of integers between 1 and N/2. If the count is greater than the number of possible integers in that range, then I know there's a duplicate in that range. Otherwise, a duplicate must exist in the range of N/2+1 to N. Once I know which half of the range the duplicate is in, I can recurse and binary search in that half, then keep repeating the process until I've found a duplicated number. The time complexity is O(n*log n) and the space complexity is O(1).

Interviewer: When can you start?



Questions like this are great because they test so many things at the same time:

    The candidate's general competence with algorithms, space/time complexity, etc.
    The candidate's ability to respond to different constraints and handle various trade-offs. This is something engineers deal with all of the time, and it's a critical skill to have.
    The candidate's creativity. Each constraint forces a person to start from scratch and think of a completely new approach -- a great test of creativity.
    The candidate's attitude toward complexity. Some candidates get permanently stuck because they start off by trying to come up with the O(n*log n) time / O(1) space solution. They assume that using a hash or comparing all elements of the list to all other elements is not what you're looking for, and so they don't mention the easy solutions (but also can't figure out the harder solutions). This is a yellow flag that the candidate tends to overcomplicate things (I'll typically ask subsequent interviewers to watch out for this tendency).
    The candidate's passion for learning and challenges. Some people get excited when you throw in harder and harder constraints, others get dejected and/or lazy.


** To give credit where credit is due, I was asked this question during an interview at Microsoft. I thought it was a great question and have been using it myself ever since. Quora seems like a good place to retire the question and force myself to think of something more original =).
