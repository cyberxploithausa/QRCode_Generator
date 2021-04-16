import qrcode

hoton_QR = qrcode.QRCode(
	version=1,
	box_size=10,
	border=5
)

sirri = "Barka da zuwa cyberploit hausa"
hoton_QR.add_data(sirri)
hoton_QR.make(fit=True)

hoto = hoton_QR.make_image(fill="black", back_color="white")
hoto.save("Bude.png")
