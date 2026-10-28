import qrcode
 
data = input("Enter text or Website link: ")
filename = input("Enter file name: ")

if filename == "":
    print("File name cannot be empty!")
else:
    qr = qrcode.make(data)
    qr.save(filename + ".png")
    print("QR Code saved as", filename + ".png")
