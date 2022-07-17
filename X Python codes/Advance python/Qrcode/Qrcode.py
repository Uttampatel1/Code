import qrcode

# Link for website

input_data = "f4810f10-4cd0-11ec-9c5c-5d301628386b"

#Creating an instance of qrcode

qr = qrcode.QRCode(
        version=15,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

#RGB color tuples
#img = qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

img.save('qrcode001.png')



'''
# read Qrcode 
import io
import qrcode
qr = qrcode.QRCode()
qr.add_data("https://utampipaliya.blogspot.com/")
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())
'''



'''
import qrcode
from qrcode.image.pure import PymagingImage
img = qrcode.make('https://utampipaliya.blogspot.com/', image_factory=PymagingImage)
'''