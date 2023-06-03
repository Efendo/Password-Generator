import random

def GeneratePassword():
    field = Element('passw-out') #init the password field
    passwrd = ""
    chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','@','_','~','+','/']
    for x in range(0, 256): #scramble 255 times
        passwrd = ""
        for i in range(0, 3):
            for j in range(0, 4):
                passwrd += chars[random.randint(0, len(chars) - 1)]

            passwrd += "-"
    for j in range(0, 4):
                passwrd += chars[random.randint(0, len(chars) - 1)]

    field.element.innerText = passwrd #display the password