import qrcode
import image

qr = qrcode.QRCode(version=15, box_size=10, border=5)
# data = "Emerson-Britto"
# data = "https://www.linkedin.com/in/emerson-britto"
data = input("Enter data (links, text, etc..): ")

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")
print("your qrcode was saved (qrcode.png)")