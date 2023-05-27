import random
guess=int(input("Guess and enter a random number between 1 to 9:"))
rand_num=random.randrange(1,10)
print(rand_num)
if(guess<rand_num):
    print("Guessed number is low")
elif(guess==rand_num):
    print("Guessed number is exactly right, well done")
else:
    print("Guessed number is high")