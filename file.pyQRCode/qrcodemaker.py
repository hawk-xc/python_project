# this program is to make qrcode image
# this program is to read qrcode image
# writen in python by wahyu tc
# you can also visit their documentation in github
# https://github.com/hawk-xc


# import module
import qrcode as qr
import cv2

def message():
    '''
    # qrcode by wahyu
    [1]. QRCode maker
    [2]. QRCode reader
    [3]. web cam QRCode reader
    '''
    pass

print (message.__doc__)
data = int(input('select options ? '))

if data == 1:
    inpname = input('qrcode text or link ? ')
    inpnamepwq = input('qrcode file name ? ')
    inpmethod = input('use default or make custom . type [y/n] ') or 'y'
    if inpmethod == 'y':
        dat = qr.make(inpname)
        pqd = dat.save(inpnamepwq+'.png')
        print ('QRCode successfully created with name', inpnamepwq+'.png')

    else:
        qrver = int(input('QRimage version[recommend is 1] ? ') or 1)
        qrimagesize = int(input('QRimage size[recommend is 10] ? ') or 10)
        qrimageborder = int(input('QRimage border size[default is 5] ? ') or 5)
        qrimagefillcolor = input('QRimage fill color[default is black] ? ') or 'black'
        qrimagefillback = input('QRimage back fill color[default is white] ? ') or 'white'
        QRDat = qr.QRCode(
            version = qrver,
            box_size = qrimagesize,
            border = qrimageborder
        )
        QRDat.add_data(data)
        QRDat.make(fit=True)
        img = QRDat.make_image(
            fill_color = qrimagefillcolor,
            back_color = qrimagefillback
        )
        img.save(inpnamepwq+'.png')
        print ('QRCode image successful create with name', inpnamepwq+'.png')

elif data == 2:
    datacv = input('insert image location and name . ')
    image = cv2.imread(datacv)
    detector = cv2.QRCodeDetector()
    datacv, vertices_array, binnary_qrcode = detector.detectAndDecode(image)
    datatab = []
    if vertices_array is not None:
        print ('QRCode result : ')
        av = datatab.append(datacv)
        print (datatab)

    else:
        print ('something was error data', datacv)
        pass
    pass

elif data == 3:
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()
    while True:
        _, img = cap.read()
        msn, vertices_array, _ = detector.detectAndDecode(img)
        if vertices_array is not None:
            if msn:
                print("QR Code detected, data:", msn)
        cv2.imshow("img", img)
        if cv2.waitKey(1) == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

else:
    print ('quit!!! error has occured')