import qrcode
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data("Enter URL here")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
#Saves image in the current repository as "qrcode.png"
img.save("qrcode.png")