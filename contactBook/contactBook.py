#contactbook
# 1 add contact
# view contact
# search contact
# update contact
# delete contacts
# exit

print('*****************************')
print('')
print('contactbook pro')
print('')
print ('')

contacts = []

def showContacts():
    for index, contact in enumerate (contacts, start = 1):
        print (f"{index}. {contact['contactName']}  -   {contact['contactNo']}   -   {contact['Email']}")

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
                    print(f' changing {contact_list['contactName']}')
                    new_name = input('input new name for contact: ')
                    contact['contactName'] = new_name
                    print('Name updated')
                elif update =='2':
                    print(f' changing {contact_list['contactNo']}')
                    new_no = input('input new number for contact: ')
                    contact['contactNo'] = new_no
                    print('Number updated')
                elif update == '3':
                    print(f' changing {contact_list['Email']}')
                    new_mail = input('input new Email for contact: ')
                    contact['Email'] = new_mail
                    print('Email updated')
                else:
                    print('invalid selection')
        
                break
        if not found:
            print('Not found')
            
    elif choice == '5':
        showContacts()
        take = int(input('enter the number of the contact to delete: '))
        del contacts[take - 1]
        print('contact deleted')




                


            







    