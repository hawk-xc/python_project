from pyzbar.pyzbar import decode
from PIL import Image
import qrcode
import time

# pip3 install pillow
# pip3 install qrcode
# pip3 install pyzbar

while True:
    print (f"\t{15*'#'} QRCode maker & decryptor {15*'#'}")
    qst = int(input('\t[1] make qrcode\n\t[2] decode qrcode\n\t[3] exit\n\toptions : '))
    if qst == 1:
        link = input('link name : ')
        name = input('image name : ')
        box = int(input('box size : ') or 10)
        border = int(input('border size : ') or 4)
        fill = input('fill color : ') or 'black'
        back = input('back color : ') or 'white'
        qr = qrcode.QRCode(
            version=1,
            box_size=box,
            border=border
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill, back_color=back)
        img.save(name+'.png')
        print (f'{name}.png successfull save!\n')
        time.sleep(1)
    
    elif qst == 2:
        img_name = input('qrcode name : ')
        decocdeQR = decode(Image.open(img_name))
        print(f"result is : [ {decocdeQR[0].data.decode('ascii')} ]")
        time.sleep(1)

    else:
        print ('\tthnx, good bye :)')
        time.sleep(1)
        break
else:
    print ('Fail')
