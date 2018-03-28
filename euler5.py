# Tommy Vaughan 12/03/2018
# Project Euler problem 5 https://projecteuler.net/problem=5
# What is the smallest number that is divisible by all of the numbers from 1 to 20?
# Found workable solution on https://gist.github.com/PEZ/47534
# Added the comments to expalin my understanding of the solution.


i = 1                       
for k in (range(1, 21)):                  # Loop through the range a number at a time
  if i % k > 0:                           
    for j in range(1, 21): 
      if (i*j) % k == 0:   
        i *= j 
        break 

print(i)

    


 
  














