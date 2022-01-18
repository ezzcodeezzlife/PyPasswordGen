import random
import string
import pyperclip

def write(password, mail, address):
    name = 'generated_passwords.txt'  
    try:
        file = open(name,'a+')
        file.write(""+  password + " " + mail + " " + address + '\n')
        file.close()
    except:
        print('file.write went wrong!')
    

class PasswordGenerator:
    def generate(self, stringlength= 16):
        password_characters = string.ascii_letters + string.digits + string.punctuation 
        password = ''.join(random.choice(password_characters) for i in range(stringlength))

        pyperclip.copy(password)
        print("Copyed password to the clipboard!", )

        print("Save additional info:")
        mail = input("Mail/Username:")
        address = input("Address:")

        write(password, mail , address)

myPasswordGenerator = PasswordGenerator()
myPasswordGenerator.generate()


    
