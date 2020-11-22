import random
import string
import pyperclip
from os.path import join
import time

def write(password, mail, address):
        name = 'generated_passwords.txt'  

        try:
            file = open(name,'a+')
            file.write(""+  password + " " + mail + " " + address + '\n')
            file.close()

        except:
            print('Something went wrong!')

def randomStringwithDigitsAndSymbols(stringLength=4):
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))


pw = input("Password to brute: ")

count = 0
start = time.time()

while True:
    generated_password = randomStringwithDigitsAndSymbols(3)
    print("Tried: ",generated_password)
    print(count)
    count = count +1
    if pw == generated_password:
        print("Done!: ", generated_password)
        end = time.time()
        print(end - start)
        break

