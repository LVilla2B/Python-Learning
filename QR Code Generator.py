import qrcode

text = str(input("Insert URL to convert into a QR code: "))
def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save("qrimg.png")

#generate_qrcode("https://github.com/LVilla2B/Python-Learning")
print("Your QR code has been generated!")