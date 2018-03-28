# Tommy Vaughan 12/03/2018
# Project Euler problem 5 https://projecteuler.net/problem=5
# What is the smallest number that is divisible by all of the numbers from 1 to 20?
# Found workable solution on https://gist.github.com/PEZ/47534
# Days have been spent on this with nothing to show, except somebody else's code :( 
# I will focus on the project instead as there are far more marks for it!


i = 1                       
for k in (range(1, 21)):                  
  if i % k > 0:                           
    for j in range(1, 21): 
      if (i*j) % k == 0:   
        i *= j 
        break 

print(i)

    


 
  














