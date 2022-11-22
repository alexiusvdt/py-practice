#we get user input by calling input() and storing that as avariable
message = input("tell me something, and i'll say it back")
print(message)

name = input("Wots yer name, laddie?")
print(f"\nPleased tae meetcha {name}")

#if long inputs required:
prompt = "if you tell me who you are, we can personalize your greeings."
prompt += "\nWhat is your name?"

#input() parses everything as a string, but what if we want numbers?
age = input("how old are ye?")
age = int(age)

height = input("how tall are you in inches? ")
height = int(height)

if height >= 48:
  print("\nYou're tall enough to ride!")
else:
  print("\nYou're too short! Try again next year")

#we can use modulo (%) to return a remainder. 7 % 3 returns 1
number = input("how tall are you in inches? ")
number = int(number)

if number % 2 == 0:
  print(f"\n the number {number} is even")
else:
  print(f"the number {number} is odd")