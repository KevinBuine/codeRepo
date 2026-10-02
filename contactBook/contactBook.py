#contactbook
# 1 add contact
# view contact
# search contact
# update contact
# delete contacts
# exit
import json
try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
except:
    FileNotFoundError
    contacts = []

print('*****************************')
print('')
print('contactbook pro')
print('')
print ('')

def showContacts():
    for index, contact in enumerate (contacts, start = 1):
        print (f"{index}. {contact['contactName']}  -   {contact['contactNo']}   -   {contact['Email']}")

def saveContacts():
    with open ("contacts.json", "w") as file:
                    json.dump(contacts, file, indent=4)
    
    

def searchContacts():
    value = input('Enter contact name to search: ')
    for index, contact in enumerate (contacts, start=1):
        if value.lower() == contact['contactName'].lower():
            print('Contact found....')
            print(f"{index}. {contact['contactName']}  - {contact['contactNo']}   -  {contact['Email']}")
            return
    print('Contact not found....')


while True:
    choice = input('welcome to Contactbook pro. what operation do you want to perform? \n1. Add contact \n2. view contacts \n3. search contacts \n4.Update contact \n 5. delete contact \n6. exit \n')
    
    if choice == '6':
        print('Thank you for using contacts')
        break

    elif choice == '1':

        while True:

            contact_name = input('Enter contact name: ')
            contact_no = input('Enter contact number: ')
            email = input('Enter email: ')
            contact_list = {
                "contactName" : contact_name,
                "contactNo" : contact_no, 
                "Email": email
            }
            contacts.append(contact_list)

            saveContacts()
            print('contact saved....')
            option = input('Do ypu want to save anoter contact? 1. Yes   2. No \n')
            if option == '2':
                break

    elif choice == '2':
        showContacts()

    elif choice == '3':

        while True:
        
            searchContacts()

            pick = input('Do you want o search again? 1. Yes   2. No')
            if pick == '2':
                break

    elif choice == '4':
        showContacts()
        selection = input('input the name of the contact to update: ')

        found = False

        for contact in contacts:
            if selection.lower() == contact['contactName'].lower():
                found = True
                print('Contact selected')
                update = input(' select 1. Update name  2. Update number   3. Update email')
                if update == '1':
                    print(f' changing {contact['contactName']}')
                    new_name = input('input new name for contact: ')
                    contact['contactName'] = new_name
                    saveContacts()
                    print('Name updated')
                elif update =='2':
                    print(f' changing {contact['contactNo']}')
                    new_no = input('input new number for contact: ')
                    contact['contactNo'] = new_no
                    saveContacts()
                    print('Number updated')
                elif update == '3':
                    print(f' changing {contact['Email']}')
                    new_mail = input('input new Email for contact: ')
                    contact['Email'] = new_mail
                    saveContacts()
                    print('Email updated')
                else:
                    print('invalid selection')
        
                break
        if not found:
            print('Not found')
            
    elif choice == '5':
        showContacts()
        try:
            take = int(input('enter the number of the contact to delete: '))
        
            if 1<= take <= len(contacts):
                del contacts[take - 1]
                saveContacts()
                print('contact deleted')
            else:
                 print('That contact does not exist')

        except ValueError:
                    print('invalid entry. Enter a number')

                    
            

        
        




                


            







    