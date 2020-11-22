import random
import string
import pyperclip
from os.path import join

def write(password, mail, address):
        name = 'generated_passwords.txt'  

        try:
            file = open(name,'a+')
            file.write(""+  password + " " + mail + " " + address + '\n')
            file.close()

        except:
            print('Something went wrong!')

def randomStringwithDigitsAndSymbols(stringLength=10):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

generated_password = randomStringwithDigitsAndSymbols(32)

print("Copyed to the clipboard! : ", generated_password)

pyperclip.copy(generated_password)

print("Save additional info:")
mail = input("Mail/Username:")
address = input("Address:")

write(generated_password, mail , address)

