import pyqrcode
import sys

def QRCreate(TextoQR, RutaQR, Size):
    qr = pyqrcode.create(TextoQR)
    qr.png(RutaQR, scale = Size)

def main():
    if len(sys.argv) != 4:
        print("Uso: QRCreate <TextoQR> <RutaQR> <Size>")
        sys.exit(1)

    TextoQR = sys.argv[1]
    RutaQR = sys.argv[2]
    Size = sys.argv[3]

    QRCreate(TextoQR, RutaQR, Size)
    print(f"¡¡¡Código QR creado exitosamente!!!\nSe ha generado el archivo: {RutaQR}")

if __name__ == "__main__":
    main()