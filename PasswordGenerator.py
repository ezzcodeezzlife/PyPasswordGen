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
            print('Something went wrong! Cannot tell what?')

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

# Your password is 32 characters long and has
# 1,380,674,536,088,650,143,049,543,431,455,155,987,400,663,734,997,083,640,156,913,664 combinations.
# It takes 26,788,611,742,835,686,924,434,482,319,313,947,415,413,212,540,043,264.00 hours
# or 1,116,192,155,951,486,955,184,770,096,638,081,142,308,883,855,835,136.00 days to crack your password on computer that trys 25,769,803,776 passwords per hour
