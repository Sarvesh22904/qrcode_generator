import qrcode

features = qrcode.QRCode(version=1, box_size=40, border=3)
features.add_data('https://vcet.edu.in/')
features.make(fit=True)
try:
    generate_image = features.make_image(fill_color="blue", back_color="white")
    generate_image.save('vcet.png')
    print("QR code generated successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
