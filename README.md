# icpc-2019-20-pacnw-d2
The problems my Division 2 Team (D2: Team1) in the Oregon State University chapter of the Association of Computer Machinery (@osu-acm). Files are labeled as `Prob<Letter of Problem>.py`. 

More details about problems (eventually) and the competition can be found at http://acmicpc-pacnw.org/.

Special thanks to Derek Williams (@derek-williams00) and Sadie Thomas (@sadiet20) for being fantastic teammates!

## Problem N: Checkerboard
Create an R-by-C grid of black and white squares based on inputs. 

### Sample Input:
    6 5 3 2
    1
    2
    3
    3
    2

### Sample Output:
    BBBWW
    WWWBB
    WWWBB
    BBBWW
    BBBWW
    BBBWW

## Problem O: Even or Odd
Your friend has secretly picked N consecutive integers between 1 and 100 and wants you to guess if their sum is even or odd or either.
Output a single word: `Even`, `Odd` or `Either`.

### Sample Inputs:
    1
    2
    3
    4

## Sample Outputs:
    Either
    Odd
    Either
    Even

## Problem Q: Dividing by Two
You are given two integres, A and B. You want to transform A to B by performing a sequence of operations. You can only perform the following operations: divide A by two, but only if A is even, or add one to A.
What is the minimum number of operations you need to transform A to B?

Sample Input | Sample Output
------------ | -------------
103 27 | 4
3 8 | 5

## Problem R: Rainbow Strings
Unfinished in the competition (November 9th, 2019). 

Define a string to be a *rainbow string* if every letter in the string is distinct. An empty string is also considered to be a *rainbow string*. Given a string of lowercase letters, compute the number of different subsequences which are rainbow strings. Two subsequences are different if an **index** is included in one subsequence but not the other, even if the resulting strings are identical.
Print out the number of rainbow sequences of the input string, modulo 11,092,019.

Sample Input | Sample Output
------------ | -------------
aab | 6
icpcprogrammingcontest | 209952

## Problem S: Speeding
You'd like to figure out if a car was speeding while driving down a straight road, but all you have are photographs taken at different locations and different times. Given numbers for time and position (always starting at 0 and 0 respectively), find the fastest speed you can prove the car was going at some point along the road.

### Sample Input
    5
    0 0
    5 24
    10 98
    15 222
    20 396

### Sample Output
    34

## Problem U: Issuing Plates
You are writing code to check license plates, consisting of combinations of uppercase letters and numbers 0-9. You want to make sure the codes do not contain any bad words, even considering leetspeak.

In leetspeak, we have the following equivalencies: `0=O 1=L 2=Z 3=E 5=S 6=B 7=T 8=B` 

Given some input strings for bad words and license plates, which are valid? For each license plate, print out `VALID` or `INVALID`.

### Sample Input
    7 2
    AWFUL
    BAD
    CRUMMY
    LOUSY
    POOR
    SAD
    TERRIBLE
    SO5OD
    TROUBADOUR

### Sample Output
    VALID
    INVALID

## Problem V: Correcting Keats
Charles's friend Keats makes lots of small errors, defined as: adding a letter anywhere in a string, removing a letter from anywhere in the string, and changing any letter in the strong to any other letter. Find all other strings that can be made.

The first line of the input contains all possible letters that can be use (an 'alphabet' of sorts).
The second line is the word that Keats will misspell.

### Sample Input
    eg
    egg

### Sample Output
    eeg
    eegg
    eg
    ege
    egeg
    egge
    eggg
    gegg
    gg
    ggg

## Problem W: Black and White
You are given an n-by-n grid where each square is colored black or white. A grid is correct if every row and every column has the same number of black squares as it has white squares. No row or column has 3 or more consecutive squares of the same color.

Given a grid, determine whether it is correct (1) or incorrect (0).

### Sample Input
    4
    WBBW
    WBWB
    BWWB
    BWBW

### Sample Output
    1

## Problem X: Remorse
A Morse-like code is an assignment of sequences of dots and dashes to alphabet characters. You are to create a Morse-like code that yields the shortest total length to a given message, and return that total length.

Type | Length
---- | ------
dot | 1
dash | 3
gap between dots and dashes within a character | 1
gap between characters | 3
spaces and punctuation | 0 (ignored)

The input will be a single line consisting of uppercase or lowercase letters, spaces, commas, periods, exclamation points and question marks. The line will have a maximum length of 32000 characters and will contain at least one letter. Everything but letters should be ignored.

The output will consist of the length of the encoded string when an optimal Morse-like code is used.

Sample Input | Sample Output
------------ | -------------
icpc | 17
The quick brown dog jumps over the lazy fox. | 335
