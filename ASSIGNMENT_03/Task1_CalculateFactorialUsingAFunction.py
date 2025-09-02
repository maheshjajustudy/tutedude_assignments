'''
Task 1: Calculate Factorial Using a Function


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

Expected Output:
For example, if the function is called with 5, it should return:
Enter a number: 3
The factorial of 3 is 6
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("The factorial of {} is {}".format(num, factorial(num)))