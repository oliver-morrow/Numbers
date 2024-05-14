'''
Program to take user input and find all prime factorizations of the number (if there are any)
'''

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

userInput = int(input("Enter a number: "))
print(primeFactors(userInput))