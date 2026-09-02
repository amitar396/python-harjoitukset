 print("Hello")
 print("World")

 

 Viivi = input('Syota nimesi: ')

 print("Terve, " + Viivi + "!")

 Ahmed = input('Syota nimesi: ')
 
 print("Terve, " + Ahmed + "!")

 import math

 radius_of_the_circle = float(input("Enter the radius of the circle: "))

 side_of_square = float(input("Enter the side length of the square: "))

import math

 radius_of_the_circle = float(input("Enter the radius of the circle: "))

 area_of_circle = (math.pi * radius_of_the_circle**2)

 print("area of circle is:",area_of_circle)


  width = float(input("Enter the width of rectangle: "))
  height = float(input("Enter the height of reactangle: "))

  area_of_rectangle = (width * height)
  perimeter_of_rectangle = 2 * (width + height)


  print(f"perimeter_of_rectangle is : {perimeter_of_rectangle:.2f}")
   print(f"area_of_rectangle is : {area_of_rectangle:.2f}")

 no1 = int(input("Enter first number: "))
 no2 = int(input("Enter second number: "))
 no3 = int(input("Enter third number: "))

 sum_of_numbers = no1+no2+no3
 product_of_numbers = (no1*no2*no3)
 average_of_numbers = (no1+no2+no3)/3


 print("sum of numbers is ", sum_of_numbers )
 print("product of numbers is ", product_of_numbers)
 print("average of numbers is", average_of_numbers)

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


 import random
   
 dice1 = random.randint(0, 9)
dice2 = random.randint(0, 9)
 dice3 = random.randint(0, 9)

 print(f"Result of the first number: {dice1}")
 print(f"Result of the second number: {dice2}")
print(f"Result of the third number: {dice3}")

 print(f"Passcode is: {dice1}{dice2}{dice3}")

 dice1 = random.randint(1, 6)
 dice2 = random.randint(1, 6)
 dice3 = random.randint(1, 6)
 dice4 = random.randint(1, 6)

print(f"Result of the first number: {dice1}")
print(f"Result of the second number: {dice2}")
print(f"Result of the third number: {dice3}")
 print(f"Result of the fourth number: {dice4}")

 print(f"Passcode is: {dice1}{dice2}{dice3}{dice4}")














