#guess the number
import random
number=random.randint(0,10)

for i in range(0,3):
    guess=int(input("Guess the number\t"))
    if guess==number:
            print(f"you won the the number was {number} correctly")
            print("you are a matka king")
            break
    else:
            print("wrong guess")
            if i==2:
                print(f"you lost the number was{number}")