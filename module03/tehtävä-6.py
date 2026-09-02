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