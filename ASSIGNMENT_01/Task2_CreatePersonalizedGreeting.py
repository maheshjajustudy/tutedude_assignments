'''
Problem Statement: Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
Expected Output:
The program should output a greeting like:

Hello, FirstName LastName! Welcome to the Python program.
'''

FirstName = input('Enter your first name: ')
LastName = input('Enter your last name: ')

print('Hello, ' + FirstName + ' ' + LastName+'! Welcome to the Python program.')