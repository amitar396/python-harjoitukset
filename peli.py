
ikä = int(input("Anna ikasi: "))

if ikä < 12:
    print("Sinulla ei riita ika, peli suljetaan.")
else:
    print("Tervetuloa peliin!")

    komento = ""
    while komento != "lopeta":
        print("--- Päävalikko ---")
        print("kerata")
        print("lajittelu")
        print("Lroska")
        print("Kirjoita 'lopeta' lopettaaksesi.")

        komento = input("Anna komento: ")

        if komento == "kerata":
            print("Hahmo keraa roskan maasta ja heittaa roskiin!")
        elif komento == "lajittelu":
            print("Hahmo laittaa oikeaan roskikseen!")
        elif komento == "Lroska":
            print("Hahmo laittaa hanskat ennen roskan keraamista!")
        elif komento == "lopeta":
            print("Peli suljetaan. Heippa!")    
        else:
            print("Tuntematon komento, yritä uudelleen.")
