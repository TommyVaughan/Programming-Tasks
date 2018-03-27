# Tommy Vaughan - 08/02/2018
# The Collatz conjecture program
# Write a script that applies the Collatz function to an interger (divide by 2 if even, multiply by 3 and add one if odd, until the interger eventually equals 1)

n = 17                        # 17 is the interger to apply the Collatz function to.

while n != 1:                 # The while loop will keep going while n is not equal to 1
    if  n % 2 == 0:           # First condition multiply by 2 if even number (even ==0)
        n = n / 2                   
        print(n)                      
    elif n % 2 == 1:          # Second condition multiply by 3 and add 1 if odd number (odd ==1)
        n = n * 3 + 1                     
        print(n)                      
    else:                     # Eventually n will equal 1 and this will end the while loop
        print(n)




   











    







 


    
