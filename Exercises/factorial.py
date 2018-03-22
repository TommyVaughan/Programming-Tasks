# Tommy Vaughan 09/03/2018
# Write a script containing factorial that takes an input of a positive integer and returns it's factorial

def factorial(n):                             # Naming the function factorial.
    if n == 1:                                
        return 1                              # factorial of 1 is one 
    else:
        return n * factorial(n-1)             # any other result will be n * n-1 which is reducing the factorial each time
n=int(input("Input a positive integer to compute the factiorial : "))  # Any positive number can be entered to check.
print(factorial(n))




