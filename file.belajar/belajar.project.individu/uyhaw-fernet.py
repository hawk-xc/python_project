#!/bin/python3
from cryptography.fernet import Fernet
import time

# maker v 0.0.1
# by uyhaw as hawk
# python3

def mkkey(key):
    skey = key+'.key'
    fkey = Fernet.generate_key()
    with open(skey, 'wb') as filekey:
        fread = filekey.write(fkey)
        filekey.close()
        print (f'\tkey length [{fread}] save as {skey}')

def encfile(key, filename):
    with open(key, 'rb') as readkey:
        keydata = readkey.read()

    fernet = Fernet(keydata)
    
    with open(filename, 'rb') as readfile:
        fdat = readfile.read()
        ffile = fernet.encrypt(fdat)

    with open(filename, 'wb') as encfile:
        encfile.write(ffile)
        encfile.close

    with open(filename, 'r') as fout_p:
        print ('*'*100)
        print (f'before\t++> [{fdat}] \nafter\t++> [{ffile}]\n\nSuccessfull save with name {filename}')

def decfile(key, filename):
    with open(key, 'rb') as readkey:
        keydata = readkey.read()

    fernet = Fernet(keydata)

    with open(filename, 'rb') as readfile:
        fdat = readfile.read()
        ffile = fernet.decrypt(fdat)

    with open(filename, 'wb') as encfile:
        encfile.write(ffile)
        encfile.close

    with open(filename, 'r') as fout_p:
        print ('*'*100)
        print (f'before\t++> [{fdat}] \nafter\t++> [{ffile}]\n\nSuccessfull save with name {filename}')

while True:
    print(f"""
    \t{'+'*8} maker {'+'*8}\t
    \t\tv 0.0.1\t\t
    """)
    time.sleep(2)

    main = input('\t[1] create key file\n\t[2] encrypt file\n\t[3] decrypt file\n\t[4] exit\n\tselect number : ')

    if main == '1':
        mkkey(input('\tkey name : '))

    elif main == '2':
        encfile(input('\tkeyname  : '), input('\tfilename : '))

    elif main == '3':
        decfile(input('\tkeyname  : '), input('\tfilename : '))
    
    elif main == '4':
        print ('\tgood bye :)')
        break
    else:
        print('\tinvalid value, exit(0)')
        time.sleep(3)
