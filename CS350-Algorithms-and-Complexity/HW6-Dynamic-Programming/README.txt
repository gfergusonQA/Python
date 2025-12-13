This project requires Python 3 and the following libraries:
- numpy

To this (clean Markdown):

```md
Install dependencies with:

```bash
pip install -r requirements.txt

## Gina Ferguson
## Assignment 6: Dynamic Programming
## Code Language: Python
## Date: 12/2/2025
## Class: CS350 Algorithms & Complexity

==================================================================

Assignment Instructions:

• Problem [24 points]
• (This problem involves coding. Submit a single zip-file with your write-up and any source code. The code should be well documented and include instructions on how to run it. If you used any reference material (found in a book or online), please include a link or citations in your write-up

• We will work on a classic coding interview problem: Find the length of the longest palindromic substring* for a given input string.

==================================================================
PART A: 

• (a) [7 points] Problem 6 (MysteryAlgorithm) in the bonus midterm solved this problem. Provide a one sentence justification for why you think that implementation does or does not belong to the following design strategies: [iterative algorithm design, divide and conquer, brute force, decrease and conquer, string processing, recursive algorithm design, decrease-by-variable-size and conquer]. Remember that an algorithm can belong to more than one design category!

Iterative Algorithm Design: No because there are not any loops, just conditional statements using if else statements and recursive calls. 
Divide and Conquer:  Yes the string is an array that is being divided into sections using conditional if else statements.
Brute Force: Yes, because it tries each possibility using if else statements.
Decrease and Conquer: Yes, because the recursive calls move the testing section around to smaller arrays to test.
String Processing: Yes, because a string is literally being processed using arrays with indices character by character and searches for a substring.
Recursive Algorithm Design: Yes, because the algorithm calls itself. 
Decrease-by-variable-size and Conquer: Yes, the substring size is decreased depending on the recursive call/section. 

==================================================================
PART B: 

• b) [5 points] Using your favorite programming language, implement a brute-force iterative algorithm that returns the length of the longest palindromic substring of a given input string. Make sure to clearly document your code and include instructions on how to run it. Show a screenshot for outputs for five example strings that each include palindromic substrings of different lengths.

See part-b.py code. 
Run the code by opening the parent folder, "HW6-Dynamic-Programming", of the code file in the terminal.
In the same terminal run command: "python3 part-b.py"  without the " " marks. 
Test away :)

=================================================================
PART C: 

• (c) [2 points] What is the asymptotic runtime of the iterative approach? What is the space complexity of the iterative approach? Your answers should be in terms of big-Theta or big-O.

Time Complexity:
Operation: All possible substrings (comparison)
    --> Outer + inner loops = Θ(n²)
Operation: Checking if Palindrome (comparison)
    --> function is_palindrome worst case: Θ(n)

Final Time Complexity:
Θ(n³)

Space Complexity: Θ(n)
2 indices, length of string variable, etc
1 temporary substring candidate, only one at a time
Worse Case: Θ(n)
This doesn't change because we are only storing 1 at a time on the side. 

Recurrence Relation:
Looping over i and j≥i
k = j - i + 1 ( cost Θ(k) )
T(n) ={ ∑[ (i=0) to (n-1) ] } * { [ ∑[ (j=i) to (n-1) ] }
Let k = j - i + 1:

T(n) = ∑[(k=1) to m] = [m(m+1)]/2
n(n+1)(n+1)/6
= Θ(n3)

Also: pal = palindrome
T(n) = n^2 * T_pal(n) = Θ(n3)

=================================================================
PART D: 

• (d) [5 points] Implement a dynamic program for the longest palindromic substring problem in your favorite programming language.

See part-d.py code.
Run the code by opening the parent folder of the code file in the terminal.
In the same terminal run the command: "python3 part-d.py"  without the " " marks.
Test away :)

=================================================================
PART E: 

• (e) [2 points] What is the asymptotic runtime of your dynamic programming approach? What is the space complexity of the dynamic programming approach? Your answers should be in terms of big-Theta or big-O.

Time Complexity:
Operation: fill memoTable (like a truth table)
--> 2 nested loops over all substring
--> outerloop (length) + inner loop (start index) = Θ(n^2) quadratic time

Operation: Dynamic Prog. recurrence
--> each cell memoTable[i][j] computed in Θ(1) Constant time
--> no substring scanned like brute force

Final Time Complexity:
Θ(n^2)

Space Complexity:
2D list of booleans --> memoTable[i][j]
no substring allocations, no recursion

Worse Case: 
--> n^2 entries
--> Θ(n^2)
Θ(n^2) because store results as you go for every substring pair

Summation:
like the:
T(n) = ∑(k = 1 to n) k
     = n(n+1)/2 {the consecutive sum of integers recurrence relation :) }
     = Θ(n^2)

=================================================================
PART F:

• (f) [3 points] Generate plots of the runtime of your iterative implementation (part b) and your dynamic programming implementation (part d) for increasing lengths of input strings (e.g. 10, 100, 1000, 10000, etc.). Show both plots on the same axis and comment on how they compare to what you expect from parts (c) and (e).

See the PDF doc in the zipped file

=================================================================
PART G:

• (g) [Bonus question] Read about Manacher's algorithm (on Wikipedia or elsewhere). Does it solve the same problem? What is its asymptotic complexity?

See the PDF in the zipped file.

=================================================================
(* A substring should not be confused with a subsequence. A substring is a set of contiguous characters located within an input string. A subsequence is any subset of characters from a string that appear in the same sequence in the string. For example, abc is a substring of yrabcbiiu but yciu is a not a substring because these characters do not occur contiguously.  However yciu is a subsequence of yrabcbiiu because these characters appear in that sequence in the longer string. )

==================================================================

