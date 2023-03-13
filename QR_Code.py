import qrcode 
import link
from PIL import Image 

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5,)
qr.add_data(link.link)
qr.make(fit=True)
color_1=input("Choise QR Code color: ")
color_2=input("Choise background color: ")
img=qr.make_image(fill_color=f"{color_1}",back_color=f"{color_2}")
img.save("01_QR_Code generater/QR_Code.png")