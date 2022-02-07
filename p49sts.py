import playsound as ps
import random as r
import os as o

ocean = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
anticounter = 0
o.system("cls")
print("welcome to my game!")
print('''you have 5 chances to guess 3 right spots''')
for i in range(0, 5):
    sea = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    rand_int = r.randint(0, len(sea)-1)
    sea[rand_int] = 1
    print(sea)
    print(f"chance number {i+1}")
    print(ocean)
    bomb = int(input("enter the location to bomb(0-10)\n"))
    location = sea[bomb]
    if location == 1:
        counter = counter+1
        print("right choice!")
        if counter == 3:
            print("you won!")
            ps.playsound('ringtones_Jigar_Mai_Beedi_Aag_Hai.mp3', True)
            break
    else:
        anticounter = anticounter+1
        print("wrong choice!")
        if anticounter == 3:
            print("you loose")
            #ps.playsound('Mere_To_L_Lag_Gaye_Jolly_Llb.mp3', True)
            break

print(f'''number of right choices {counter}
number of wrong choices {anticounter}''')
