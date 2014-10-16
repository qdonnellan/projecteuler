# projecteuler

*Note: I am currrently refactoring this project to reflect what I've leared from reading Robert Martin's "Clean Code"*

These are my implementations of the [Project Euler](http://projecteuler.net/) problems is a few different languages. My goal for the immediate future is to present implementations for the first 25 problems in **Python**, **Go** and **Javascript**. 

## Why Project Euler?
As it turns out, project euler problems are a great place for a beginner to learn how to code in a new language *while simultaneously learning test driven development*. Take a look at PE's first problem statement:

>If we list all the natural numbers below 10 
>that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
> The sum of these multiples is 23. 
> Find the sum of all the multiples of 3 or 5 below 1000.

Did they just give me a test case before a problem statement? **Yes they did**, and I think that is awesome. 

## What I am doing
For each problem on Project Euler, I first look at the test case (and, by the way, every project euler problem I have come across lists an easy to verify test case). Then I write a test case for that problem **before I write a solution**. For example, the first thing I will write for problem 1 will be this (if I'm doing it in Python)

    import unittest
    from problem_01 import sum_three_five
    
    class Problem01Test(unittest.TestCase):
        """
        testing my implementation of problem 1
        """
        
        def test_the_simple_test_case(self):
            """
            the sum of all ints less than 10 that are multiples of 3 or 5
            should be 23
            """
            self.assertEqual(23, sum_three_five(10))
           
If you want to force yourself to start learning test driven development, you could probably do a lot worse that working through each Project Euler problem one test at a time. You don't even have to come up with the test cases since they are already written for you by PE!

## Current Implementations

### Javascript
Depends on `node`. Testing is done using `mocha`

### Python
Testing is done using `nose`

### Go
Testing is done using the core `go test`
