# Quiz Application Made By Nabeel And Afzal
import os as o
import operator
high_score = {}


def main():
    o.system("cls")
    print("\t\t\t\t\t\t*** QUIZ APPLICATION ***")
    print("\t\t\t\t\t\t      [1] Take a quiz")
    print("\t\t\t\t\t\t      [2] View Leaderboard")
    print("\t\t\t\t\t\t      [0] Exit")
    choice = int(input("\t\t\t\t\t\t        > Enter your choice: "))

    if choice == 1:
        Quiz()
    elif choice == 2:
        High_Score()
    elif choice == 0:
        quit()
    else:
        print("\t\t\t\t\t\t      Invalid")


def Quiz():
    Score = 0
    o.system("cls")
    print("\t\t\t\t\t\t*** QUIZ APPLICATION ***")
    name = input("\t\t\t\t\t\t      Enter your Name : ")
    print("\t\t\t\t\t\t      [A] Who is the president of India?")
    print("\t\t\t\t\t\t      [1] Narendra Modi")
    print("\t\t\t\t\t\t      [2] Raj Thakere")
    print("\t\t\t\t\t\t      [3] RajNath Kovind")
    print("\t\t\t\t\t\t      [4] Udai Sampath")
    choice_a = int(input("\t\t\t\t\t\t      Enter your choice : "))
    if choice_a == 3:
        Score += 1

    o.system("cls")
    print(
        "\t\t\t\t\t\t      [B] Grand Central Terminal, Park Avenue, New York is the world's")
    print("\t\t\t\t\t\t      [1] largest railway station")
    print("\t\t\t\t\t\t      [2] highest railway station")
    print("\t\t\t\t\t\t      [3] longest railway station")
    print("\t\t\t\t\t\t      [4] Udai Sampath")
    choice_b = int(input("\t\t\t\t\t\t      Enter your choice : "))

    if choice_b == 1:
        Score += 1

    o.system("cls")
    print(
        "\t\t\t\t\t\t      [C] First man to walk on the surface of moon")
    print("\t\t\t\t\t\t      [1] Neil Armstrong")
    print("\t\t\t\t\t\t      [2] Buzz Aldrin")
    print("\t\t\t\t\t\t      [3] Jay Cutler")
    print("\t\t\t\t\t\t      [4] Adward Hawkman")
    choice_c = int(input("\t\t\t\t\t\t      Enter your choice : "))

    if choice_c == 1:
        Score += 1

    o.system("cls")
    print(
        "\t\t\t\t\t\t      [D] Best Classes for coding")
    print("\t\t\t\t\t\t      [1] Zyan Academy")
    print("\t\t\t\t\t\t      [2] Visual Labs")
    print("\t\t\t\t\t\t      [3] Crescent Classes")
    print("\t\t\t\t\t\t      [4] Succes Classes")
    choice_d = int(input("\t\t\t\t\t\t      Enter your choice : "))
    if choice_d == 2:
        Score += 1

    o.system("cls")
    print(
        "\t\t\t\t\t\t      [E] Which of the following is not a programming lamguage?")
    print("\t\t\t\t\t\t      [1] HTML")
    print("\t\t\t\t\t\t      [2] JAVA")
    print("\t\t\t\t\t\t      [3] C#")
    print("\t\t\t\t\t\t      [4] Python")
    choice_e = int(input("\t\t\t\t\t\t      Enter your choice : "))
    if choice_e == 1:
        Score += 1
    o.system("cls")
    print(f"\t\t\t\t\t\t      {name} You got {Score} out of 5")
    high_score[name] = Score

    print("\t\t\t\t\t\t      [1] Main Menu")
    print("\t\t\t\t\t\t      [2] Exit")
    nav = int(input("\t\t\t\t\t\t      Enter your choice : "))
    if nav == 1:
        main()
    elif nav == 2:
        quit()


def High_Score():
    o.system("cls")
    sorted_score = dict(
        sorted(high_score.items(), key=operator.itemgetter(1), reverse=True))
    for name, scores in sorted_score.items():
        print("\t\t\t\t\t\t      NAME: "+name+" SCORE: ", scores)

    print("\t\t\t\t\t\t      [1] Main Menu")
    print("\t\t\t\t\t\t      [2] Exit")
    nav = int(input("\t\t\t\t\t\t      Enter your choice : "))
    if nav == 1:
        main()
    elif nav == 2:
        quit()


main()
