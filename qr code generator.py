import qrcode

data= input("ender data o rurl: ").strip()
filename=input('enter filename: ').strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(file_color='black',back_color='white')
image.save(filename)
print(f'qr code saved as {filename}')