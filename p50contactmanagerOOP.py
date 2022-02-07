
class ContactManager():
    def __init__(self):
        print("Contact Manager created")
        self.contact_list = {}

    def add_contact(self):
        self.name=input(" enter Name\t")
        self.mobile_number=input(" enter Mobile Number\t")
        print(f"Adding contact {self.name} {self.mobile_number}")
        self.contact_list[self.name] = self.mobile_number
        print("Contact added")
        
    def print_contact(self):
        self.name=input("Name")
        if self.name in self.contact_list:
            print("printing contact")
            print(self.name+" "+self.contact_list[self.name])
        else:
            print("Contact not found in contact list")
            
    def print_contacts(self):
        print("printing all contact")
        for self.name, self.mobile_number in self.contact_list.items():
            print(self.name, self.mobile_number)
            
    def search_contact(self):
        self.name=input("enter name\t")
        print(f"searching contact {self.name}")
        if self.name in self.contact_list:
            print("Contact found")
            print(self.name+" "+self.contact_list[self.name])
        else:
            print("Contact not found in searching")
            
    def delete_contact(self):
        self.name=input("enter name\t")      
        if self.name in self.contact_list:
            del self.contact_list[self.name]
            print("Contact deleted")
        else:
            print("Contact not found for deleting")
            
    def update_contact(self):
        self.name=input("enter name\t")      
        self.mobile_number=input(" enter Mobile Number\t")
        if self.name in self.contact_list:
            self.contact_list[self.name] = self.mobile_number
            print("Contact updated")
        else:
            print("Contact not found for updating")
