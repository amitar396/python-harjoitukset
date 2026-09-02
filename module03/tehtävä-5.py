leiviskat = float(input("Anna leiviskat: "))
naulat = float(input("Anna naulat "))

luodit = float(input("Anna luodit "))

luodit_g = luodit * 13.3
naulat_g = naulat * 32 * 13.3
leiviska_g = leiviskat * 20 * 32 * 13.3

yhteensa_gramma = luodit_g + naulat_g + leiviska_g
kilogramma = int(yhteensa_gramma // 1000)
gramma = yhteensa_gramma % 1000

print(f"massa nykymittojen mukaan: {kilogramma} kilogrammaa ja {gramma:.2f} grammaa.")