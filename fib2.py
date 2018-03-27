# Tommy Vaughan
# A program that displays Fibonacci numbers using people's names.
# Exercise 1: My name is Tommy, so the first and last letter of my name (T + Y = 20 + 25) give the number  45. 
# The 45th Fibonacci number is 1134903170"
# Exercise 2: Below is an expansion of the fib exercise mentioned in the above comments. 
# The program was written by Ian McLoughlin and I have changed the string variable to contain my own surname.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Vaughan"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
