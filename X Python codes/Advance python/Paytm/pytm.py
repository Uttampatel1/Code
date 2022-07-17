
import qrcode

# Link for website

input_data = "cWjccdoDU1XSSC49GbFKuChq3ATAyJDzHOIi8YiTLKQP/LL4h3aOpxl6/xea/YLpmUkcZveQ7H0lYPItaPFbI9GZL+fEadiK"

#Creating an instance of qrcode

qr = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5)

qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")