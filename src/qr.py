import io
import qrcode
import os

## Salida a prod
print("Generando codigo QR")

if __name__ == '__main__':
    qr = qrcode.QRCode()
    qr.add_data("hola mundo desde github")
    file = io.StringIO()
    qr.print_ascii(out=file)
    file.seek(0)
    print(file.read())