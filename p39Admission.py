# 2)wap to accept admission of 5 students by taking the inputs from the
# user and store it in a dictionary
# later 0ne of the student cancel the addmission so print
# the complete name of the student

import os
def clear(): return os.system('cls')


student_list1 = ["", "", "", ""]
student_list2 = ["", "", "", ""]
student_list3 = ["", "", "", ""]
student_list4 = ["", "", "", ""]
student_list5 = ["", "", "", ""]

students_lists = [student_list1, student_list2,
                  student_list3, student_list4, student_list5]


students_details = {1: student_list1, 2: student_list2,
                    3: student_list3, 4: student_list4, 5: student_list5}


def main():

    clear()

    print("***** WELCOME TO CODING SCHOOL *****")
    print("      [1] DO ADDMISSION.")
    print("      [2] Display Students List.")
    print("      [3] Cancel Admission.")
    print("      [4] Enter 0 to exit.")
    print("        > Enter your choice : ", end="")
    choice = int(input())

    if choice == 1:
        do_admission()
    elif choice == 2:
        print_list()
    elif choice == 3:
        cancel_admission()
    elif choice == 0:
        print("      EXITED.")
        quit()


def do_admission():

    clear()

    print("***** ADMISSION CENTER *****")
    for i in range(0, 5):
        print("Enter the details of ", i+1, " student")
        print("your unique id is", i+1)
        last_name = input("          last name : ")
        students_lists[i][0] = last_name

        first_name = input("         first name  : ")
        students_lists[i][1] = first_name

        father_name = input("        father name  : ")
        students_lists[i][2] = father_name

        mother_name = input("        mother name  : ")
        students_lists[i][3] = mother_name
        clear()
    main()


def cancel_admission():
    clear()
    print("***** CANCLE ADMISSION *****")
    cancel = int(input("Enter your unique id : "))
    student_cancel_key = students_details.get(cancel)
    print(student_cancel_key)

    for i in range(0, 4):
        student_cancel_key[i] = ""

    print("Chal nikal dobaara shakal mat dikhana bohat marunga ")
    choice = input("Do you want to return to main page? ")
    if choice == "yes":
        clear()
        main()
    elif choice == "no":
        quit()


def print_list():

    def clear(): return os.system('cls')
    clear()

    print("***** STUDENTS DETAILS *****")

    for p, v in students_details.items():
        print("Student", p, v)

    choice = input("Do you want to return to main page? ")
    if choice == "yes":
        clear()
        main()
    elif choice == "no":
        quit()


main()
