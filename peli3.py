def kerata(inventaario):
    roska = input("Minkä roskan keräät? ")
    inventaario.append(roska)
    print(f"Hahmo keräsi roskan '{roska}' maasta!")


def lajittelu(inventaario):
    if len(inventaario) == 0:
        print("Inventaario on tyhjä, kerää ensin roskia!")
    else:
        inventaario.sort()
        print("Hahmo lajittelee roskat oikeisiin roskiksiin:")
        for roska in inventaario:
            print(roska)


def lroska():
    print("Hahmo laittaa hanskat ennen roskan keräämistä!")


ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Sinulla ei riitä ikä, peli suljetaan.")
else:
    print("Tervetuloa peliin!")

    inventaario = []
    komento = ""

    while komento != "lopeta":
        print("--- Päävalikko ---")
        print("kerata")
        print("lajittelu")
        print("Lroska")
        print("Kirjoita 'lopeta' lopettaaksesi.")

        komento = input("Anna komento: ").strip()

        if komento == "kerata":
            kerata(inventaario)
        elif komento == "lajittelu":
            lajittelu(inventaario)
        elif komento == "Lroska":
            lroska()
        elif komento == "lopeta":
            print("Peli suljetaan. Heippa!")
        else:
            print("Tuntematon komento, yritä uudelleen.")