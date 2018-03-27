# Tommy Vaughan - 19/02/2018
# Sum all the even numbers from 1 to 100

sum = 0
i = 0

while i <= 100:
    if i % 2 == 0:
        sum = sum + i
    i = i + 1

print("The sum of the even numbers from 1 to 100 is:", sum)    
