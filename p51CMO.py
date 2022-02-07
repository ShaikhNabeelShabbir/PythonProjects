import p50contactmanagerOOP as cmo
import os

os.system("cls")
print("Welcome to My Contact Manager")
mycontact = cmo.ContactManager()

while True:
    print('''1)ADD CONTACT
             2)CHECK CONTACT
             3)FULL LIST
             4)SEARCH
             5)DELETE CONTACT
             6)UPDATE CONTACTS
             7)QUIT''')
    choice = int(input("Enter your choice\t"))
    if choice == 1:
        mycontact.add_contact()
    elif choice == 2:
        mycontact.print_contact()
    elif choice == 3:
        mycontact.print_contacts()
    elif choice == 4:
        mycontact.search_contact()
    elif choice == 5:
        mycontact.delete_contact()
    elif choice == 6:
        mycontact.update_contact()
    elif choice == 7:
        quit()
    else:
        print("Please enter a valid choice")