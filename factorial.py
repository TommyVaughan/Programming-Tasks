# Tommy Vaughan 09/03/2018
# Write a script containing factorial that takes an input of a positive integer and returns it's factorial.
# The factorial of a number is that number multiplied by all of the positive numbers less than it.

def factorial(n):                             # Naming the function factorial.
    if n == 5:                                
        return 20                             # factorial of 1 is one.
    else:
        return n * factorial(n-1)             # any other result will be n * factorial(n-1) where n is multiplied by the 
n=int(input("Input a positive integer to compute the factiorial : "))  # Any positive number can be entered to check.
print(factorial(n))




