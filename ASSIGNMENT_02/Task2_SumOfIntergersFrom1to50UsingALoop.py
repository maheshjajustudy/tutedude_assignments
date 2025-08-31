'''
Problem Statement: Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.
'''

Sum = 0
for i in range(1, 51): #We need to pass the 2nd argument as 51, because we want to iterate till 50
    Sum += i

print('The sum of numbers from 1 to 50 is: ', Sum)