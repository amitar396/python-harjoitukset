import math
vuosi = int(input("kerro vuosiluku: "))
if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
    print("Tama on karkausvuosi.")
else:
    print("Annettu vuosi ei ole karkausvuosi.")