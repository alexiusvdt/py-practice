# we can store multiple dictionaries in a list, or a list of all items as a value in a dictionary. 
# even dictionaries can be nested in other dictionaries.

alien_0 = {'color':'green', 'points': 0}
alien_1 = {'color':'green', 'points': 0}
alien_2 = {'color':'green', 'points': 0}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
  print(alien)

#we can create multiple entries at once using range():

aliens = []

for alien_number in range(30):
  new_alien = {"color":"green", "points":5, 'speed':'slow'}
  aliens.append(new_alien)

for alien in aliens[:5]:
  print(alien)
print("...")

#show how many using len
print(f"Total number of aliens: {len(aliens)}")

#we can also modify elements within by adding this block after the code in lines 17-19
for alien in aliens[:3]:
  if alien['color'] == "green":
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10

#this modifies the first three aliens by specifying a slice in line 29.

#lists in dictionaries. not sure why this is erroring here...
pizza = {'crust' = 'thick', 'toppings':['mushrooms', 'extra cheese', 'peppers'],}

print(f"You ordered a {pizza["crust"]}-crust pizza "
  "with the following toppings:"

for topping in pizza['toppings']:
  print(f"\t{topping}")
)

#dictionary key crust has a single value, but key toppings is set up as an array value which itself holds multiple values.
