#A game which asks you to guess a number within three tries
import random
number = random.randint(1,10)

name = input("Enter your name: ")
limit = 1
print("Hey {}! Guess a number in my mind which is in between 1 and 10".format(name))
print("You only have three chances.")

while(limit<=3):
    guess = int(input())
    limit+=1
    if guess<number:
        print("Your guess is too low")
    elif guess>number:
        print("Your guess is too high")
    elif guess==number:
        break

if guess == number:
    print("Yay! you guessed the number in {} tries".format(limit))
else:
    print("You didn't guess the number. the number was ", str(number))
  
