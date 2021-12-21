import pyqrcode
import os
from os import system, name

os.system("clear")
print("----------------------------------------");
print("> QR CODE GENERATOR <")
print("Creator: rndwst\n")

link = str(input("ISI QR CODENYA: "))

url = pyqrcode.create(link)
url.png(f'{link}.png', scale = 5)
print(url.terminal())
print('QR code yang kamu minta nih ngab!')

print("----------------------------------------");
