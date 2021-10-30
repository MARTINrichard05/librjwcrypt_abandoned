import getpass

print("this is an app to encrypt data")
print("make sure to respect the following for your cybersecurity:")
print("----")
print('MAKE SURE YOU ARE NOT FILMED')
print("----")
print("MAKE SURE THAT YOU D'ONT HAVE ANY VIRUS,KEYLOGGER,ROOTKIT IT CAN COMPROMISE YOUR ENCRYPTION KEY AND ALL YOUR DATA")
print("----")
print("IF YOU LOSE YOUR ENCRYPTION KEY YOUR DATA IS LOST")
print("----")
print("if it show an error just restart it is because there is an error with a special character that idk lol")

import getpass4
import os.path
import librjwcrypt

def save(data,file):
    file = open(file, "w")
    file.write(str(data))

if os.path.isfile("crypted.txt"):
    crypted = "".join(map(str,librjwcrypt.readfile("crypted.txt")[0]))
    print("fichier existant")
    out = ""
    out = out.join(librjwcrypt.crypt("de", librjwcrypt.devkey(input("the key :")), crypted))
    print(out)

else:
    print("file d'ont exist create :  crypted.txt  in the folder of main script then enter the data you want to encrypt")
    d = input(": ")
    k = (librjwcrypt.genrndmkey())
    print("here is your key:", k)
    kc = librjwcrypt.devkey(k)
    fd = librjwcrypt.crypt("en", kc, d)
    save(fd, "crypted.txt")