import random

computer = random.randint(1, 10)

won = False
for i in range(3):
    guess = int(input("Guess a number (1-10): "))

    if guess == computer:
        print("Correct Guess!")
        won = True
        break
    elif guess > computer:
        print("Too High!")
    else:
        print("Too Low!")

if won == True:
    print("You Win!")
else:
    print("Game Over! You Lost.")