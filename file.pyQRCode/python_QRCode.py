from pyqrcode import *
import os

url_name = input('url or link name : ')
image_name = input('image name : ')
ima_dat = input('image scale [10] recomended : ')
image_data = image_name+'.png'

dat = pyqrcode.create(url_name)
dat.png(image_data, ima_dat)

if True:
    print ('success,', image_data,  'save in directory', os.path.dirname(os.path.abspath(image_data)))