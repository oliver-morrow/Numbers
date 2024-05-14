'''
A program that generates the Fibonacci sequence up to a certain number
Recall: The Fibonacci sequence is a series of numbers in which each number 
is the sum of the two preceding ones, usually starting with 0 and 1.
'''

userInput = int(input("Enter a number"))
print("The program will generate The Fibonacci sequence up to", userInput)

a, b = 0, 1

while a <= userInput:
    print(a, end=' ')
    a = b
    b = a+b