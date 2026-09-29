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
    for index, v in enumerate (contacts, start = 1):
        print (f'{index}. {contact_list['contactName']}  -   {contact_list['contactNo']}   -   {contact_list['Email']}')

def searchContacts():
    value = input('Enter contact name to search: ')
    contact = []
    for index, contact in enumerate (contacts, start=1):
        if value == contact_list['contactName']:
            contact.append(contact_list['contactName'])
        if contact:
            print('Contact found....')
            print(f"{index}. {contact}")
        else:
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
        for item in contacts:
            if selection == contact_list['contactName']:
                print('Contact selected')
                update = input(' select 1. Update name  2. Update number   3. Update email')
                if update == '1':
                    print(f' changing {contact_list['contactName']}')
                    new_name = input('input new name for contact: ')
                    contact_list['contactName'] = new_name
                    print('Name updated')
                elif update =='2':
                    print(f' changing {contact_list['contactNo']}')
                    new_no = input('input new number for contact: ')
                    contact_list['contactNo'] = new_no
                    print('Number updated')
                elif update == '3':
                    print(f' changing {contact_list['Email']}')
                    new_mail = input('input new Email for contact: ')
                    contact_list['Email'] = new_mail
                    print('Email updated')
                else:
                    print('invalid selection')
            else:
                print('Not found')
                break

    elif choice == '5':
        showContacts()
        take = input('enter the number of the contact to delete: ')
        del contacts[take - 1]
        print('contact deleted')




                


            







    