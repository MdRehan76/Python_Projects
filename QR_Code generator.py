import qrcode
from PIL import Image

qr = qrcode.QRCode(version = 1,
                   error_correction= qrcode.constants.ERROR_CORRECT_H,
                   box_size = 20, border = 4)

qr.add_data("https://github.com/MdRehan76")
qr.make(fit=True)

img = qr.make_image(fill_color = "pink",back_color = "Black")
img.save("Rehan_GitHub_Profile.png")
print("The QRCode is generated successfully")

