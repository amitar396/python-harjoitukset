biologinen_sukupuoli = input("Kerro sinun biologinen sukupuoli ")
hemoglobiiniarvo = float(input("Kerro sinun hemoglobiiniarvo "))
if biologinen_sukupuoli == "nainen":
        if hemoglobiiniarvo <117:
            print("hemoglobiiniarvo on alhainen.")
        elif hemoglobiiniarvo >175:
            print("hemoglobiiniarvo on korkea.")
        else:
            print("hemoglobiiniarvo on normaali")
if biologinen_sukupuoli == "mies":
        if hemoglobiiniarvo <134:
            print("hemoglobiiniarvo on alhainen.")
        elif hemoglobiiniarvo >195:
            print("hemoglobiiniarvo on korkea.")
        else:
            print("hemoglobiiniarvo on normaali")


            








