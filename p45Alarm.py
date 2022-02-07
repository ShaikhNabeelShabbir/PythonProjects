# create an alarm clock using python

from time import strftime
import time as t
import os
import playsound as playsound
from turtle import goto

# import required module
from pydub import AudioSegment
from pydub.playback import play


def get_time():
    os.system("cls")
    time = strftime("%I:%M")
    print("***** CLOCK *****")
    print("      ", time)
    go_to = input("      Do you want to go back to main page? yes, no : ")
    if go_to == "yes":
        main()
    elif go_to == "no":
        quit()


def set_alarm():
    os.system("cls")
    user_time = input("      Enter the time to set the alarm HH:MM ")
    print("      Alarm set for :", user_time)
    while True:
        if user_time == strftime("%I:%M"):
            print("      Alarm")
            playsound.playsound('ringtones_Jigar_Mai_Beedi_Aag_Hai.mp3', True)
            break


def main():
    os.system("cls")
    print("***** CLOCK *****")
    print("      [1] Show Time.")
    print("      [2] Set Alarm.")
    print("      [3] Exit.")
    choice = int(input("      Enter your choice : "))

    if choice == 1:
        get_time()
    elif choice == 2:
        set_alarm()
    elif choice == 3:
        quit()
    else:
        print("Invalid Choice")


main()


# for playing note.wav file
