"""
Simple program for phonebook
"""

import json

f = open("C:\\Users\\Habibul\\Desktop\\Projects\\phonebook\\book.txt", 'w+') # opens the specific phonebook file from computer
phone_book = {} # Creates empty dictionary
command = ""  # placeholder for input command

while command != 'exit':
    command = input('Enter a command \n(options:new,get,save, exit):')
    if command == "new":
        name = input('Enter name of the person:')
        p = input('Phone number: ')
        a = input('Address: ')
        phone_book[name] = {'Phone': p, 'Address': a}
        f.write(json.dumps(phone_book[name])) # in order to write the user input 
    elif command == 'get':
        name = input('Enter name of the person:')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('Entry not found in the address book')
    elif command == 'save':
        f.write(json.dumps(phone_book))
