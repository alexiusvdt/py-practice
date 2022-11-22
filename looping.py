user_0 = {
  "username":"efermi",
  "first":"enrico",
  "last":"fermi",
}

for key, value in user_0.items():
  print(f"\nkey: {key}")
  print(f"Value: {value}")

  #.items() returns a list of key/value pairs, the for loop then assigns each to the two variables provided.
  #we can also name key/value to other things for clarity:
  favorite_languages = {
  'jen':'python',
  'markus': "javascript",
  "todd": "COBOL",
  "megan": "ruby"
}

for name, language in favorite_languages.items():
  print(f"{name.title()}'s favorite language is {language.title()}.")
#this is the same as writing for name in favorite_languages.keys():

#we can selectively print items in the dictionary that match our targeted list:

friends = ['jen', 'todd']
for name in favorite_languages.keys():
  print(f"Hi {name.title()}")

  if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, i see you love {language}")
#at 26 we set a list of friends that we want a different message for. it looks through the keys and applies the correct logic
#based on whether or not it finds a match

#we can also use .keys() to search through the keys and find out if someone was asked:
if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!")

# keys() returns a list of all the keys and the if code checks the list
# looping through is always done start to finish, but we can sort things out as needed.
#we can use values() to similarly return a list of all values if we want to look through a target

for language in favorite_languages.values():
  print(language.title())

# we can wrap things inside set() to check for duplicates. it will only introduce an element once so we dont get repeats:
languages = {'python', 'ruby', 'python', 'javascript'}
for language in set(favorite_languages.values()):
  print(language.title())




