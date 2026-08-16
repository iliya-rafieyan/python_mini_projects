# Phonebook

contacts = []

def add_contact():
    name = input('Enter name : ')
    p_numbere = input('Enter phone number : ')

    contact = {
        'name':name,
        'phoneNumber':p_numbere
    }

    contacts.append(contact)
    print('Your contact added !')

def show_contacts():
    if len(contacts) == 0:
        print('No contacts !')
    else :
        for index , contact in enumerate(contacts , start=1):
            print(index , f'{contact['name']} : {contact['phoneNumber']}')

def delete_contact():
    name = input('Enter name : ')
    for i in contacts : 
        if i['name'] == name:
            contacts.remove(i)
            print(f'{name} deleted !')
        

while True:
    Choice = input('''Choose one : 
    [0] Add contact
    [1] Show contacts 
    [2] Delete contact
    >>> ''')

    if Choice == '0':
        add_contact()
    elif Choice == '1':
        show_contacts()
    elif Choice == '2':
        delete_contact()
