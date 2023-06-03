# Password Generator
 this is a website that generates a password.

 ## The Algorithm:
 ````
import random

def GeneratePassword():
    field = Element('passw-out') #init the password field
    passwrd = ""
    chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    for j in range(0, 8):
        passwrd += chars[random.randint(0, len(chars) - 1)]
    for j in range(0, 3):
                passwrd += "-"
                for i in range(0, 4):
                    passwrd += chars[random.randint(0, len(chars) - 1)]
    passwrd += "-"
    for j in range(0, 12):
        passwrd += chars[random.randint(0, len(chars) - 1)]
    field.element.innerText = passwrd #display the password
 ````
