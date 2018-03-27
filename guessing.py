# Tommy Vaughan, 18/02/2018
# Guessing Game

target = 6
guess = 4

while guess != target:
    guess = int(input("Please enter your guess:"))
    if guess == target: 
        print ("Well done! You guessed correctly")
    elif guess < target:
        print("Too low!") 
    else:
        print("Too high!")    
