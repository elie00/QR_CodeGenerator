import qrcode
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version=5,
    error_correction=ERROR_CORRECT_L,
    box_size=9,
    border=8,
)

qr.add_data('https://www.youtube.com')
qr.make(fit=True)

img = qr.make_image(fill_color="black", black_color="white")
img.save('qrcode.png')


#img = qrcode.make("https://www.youtube.com/")
#img.save("youtubeQR.jpg")

