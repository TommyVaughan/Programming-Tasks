# Tommy Vaughan 01/03/2018
# Project Euler Problem 1 
# https://projecteuler.net/archives
# Find the sum of all the multiples of 3 or 5 below 1000.


sum = 0
i = 1

while i < 1000:
  if i % 3 == 0:
    sum = sum + i
  elif i % 5 == 0:
    sum = sum + i
  i = i +1

print("Sum of multiples of 3 and 5, less then 1000:", sum)     

