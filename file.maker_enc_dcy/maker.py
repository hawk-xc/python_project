import os
import time
from cryptography.fernet import Fernet

# data encrypt and decrypt code
# make and delete any file
# wahyu hawk

# argument
def message():
    # array table
    data = list([
    '[1] create file',
    '[2] create key file',
    '[3] encrypt file by name',
    '[4] decrypt file bt name',
    '[5] delete some file',
    '[6] read file content',
    '[7] install module'
    ])
    for i in data:
        print (i)
        time.sleep(0.2)
        '''
        data
        query
        is
        data
        '''
message()
try:
    input_data = int(input('select option : '))
    if input_data != data:
        print ('!!!not in value!!!')
except:
    print ('!!!insert number in command!!!')


# data option
if input_data == 1:
    data = input('input name file, format in [.txt] : ')
    text = input('input your data into this file! : ')
    if os.path.exists(data):
        qst = input('remove file exist?\ny/n\n> ')
        if qst != "y":
            print ('file exist, failed!')
        else:
            with open(data, 'w') as fileadd_:
                fileadd_.write(text)
                fileadd_.close()
                print ('file successful add and write!')
    else:
        pass

elif input_data == 2:
    keyname = input('input name filekey, format in [.key] : ')
    key = Fernet.generate_key()
    if os.path.exists(data):
        qst = input('remove file exist?\ny/n\n> ')
        if qst != "y":
            print ('file exist, failed!')
        else:
            with open(keyname, 'wb') as filekey_:
                filekey_.write(key)
                print ('filekey successful added!, this is your filekey -')
                filekey_.close()

            with open(keyname, 'r') as keyread_:
                print (keyread_.read())
    else:
        pass

elif input_data == 3:
    fileenc = input('select name file can be encrypt : ')
    KEYENC = input('your keyfile name : ')
    with open(KEYENC, 'rb') as fileenc_:
        keypass = fileenc_.read()

    fernet = Fernet(keypass)

    try:
        with open(fileenc, 'rb') as filecanbeenc_:
            orig = filecanbeenc_.read()
            encrypt = fernet.encrypt(orig)

        with open(fileenc, 'wb') as encrypted_file_:
            encrypted_file_.write(encrypt)
            print (fileenc, 'successful decrypt!')
    except:
        print ('failure')
        pass

elif input_data == 4:
    print ('decrypt the encrypted file, ofcourse with keyfile')
    filetodec_ = input('input your encrypted file : ')
    decfilkey_ = input('input your filekey name : ')
    with open(decfilkey_, 'rb') as fileenc_:
        DECKEY = fileenc_.read()

    fernet = Fernet(DECKEY)
    try:
        with open(filetodec_, 'rb') as enc_file_:
            encrypted_ = enc_file_.read()
            
            decrypted_ = fernet.decrypt(encrypted_)

        with open(filetodec_, 'wb') as dec_file_:
            dec_file_.write(decrypted_)

            print (filetodec_, 'successful to decrypt')
    
    except:
        print ('failure')

elif input_data == 5:
    print ('this is just can delete file not folder')
    filetodel_ = input('delete file >> ')
    os.remove(filetodel_)
    print ('success remove', filetodel_)

elif input_data == 6:
    print ('this code can read readable file, insert the file and type encode [r] and this code and work for u, from wahyu')
    readfile = input('input file can be read : ')
    try:
        with open(readfile, 'r') as readfileenc_:
            print ('data file ; ')
            print (readfileenc_.read())
    except:
        print ('file error and maybe not readable')

elif input_data == 7:
    print ('install module requirement\n[os]\n[cryptography\n[time]')
    f_ = input('start install > [y/n]\n-> ')
    if f_ != "y":
        pass

    else:
        os.system('pip install cryptography')
        print ('success installed!')