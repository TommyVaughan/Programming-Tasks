# Tommy Vaughan
# Project Euler problem 5 https://projecteuler.net/problem=5
# What is the smallest number that is divisible by all of the numbers from 1 to 20?
# Found workable solution on https://gist.github.com/PEZ/47534
# Added the comments to expalin my understanding of the solution.


i = 1                       
for k in (range(1, 21)):   # k can be any value from 1 to 20
  if i % k > 0:            # if i / k > 0, which all numbers in the range are as the number "j" is divisible by all numbers k
    for j in range(1, 21): # j is the value we are looking for 
      if (i*j) % k == 0:   # i * j - no I'm lost
        i *= j 
        break 

print(i)

    


 
  














