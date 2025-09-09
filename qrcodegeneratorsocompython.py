
import qrcode
name= input("Digite o nome do arquivo (sem extensão): ")
link = input("Digite o link para gerar o QR Code: ")

qr = qrcode.make(link)
qr.save(name + ".png")

print("QR Code salvo como", name + '.png')
