#dice roll simulator

import random as r

while True:
    print("1)Roll the dice\n2)quit")
    user=int(input("Enter your choice: "))
    if user==1:
        print("Rolling the dice...")
        print(r.randint(1,6))
    elif user==2:
        break
    else:
        print("invalid input")