pituus = float(input("Anna kuhan pituus (cm):"))
if pituus > 37:
    print("Otetaan kuha mukaan!")
else:
    puuttuu = 37 - pituus    
    print(f"Voi laskea kuhan takaisin järveen, koska se on alamittainen ja siitä puuttuu {puuttuu} cm!")

 