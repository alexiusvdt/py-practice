# dictionaries are collections of key-value pairs
alien_0 = {'color':'green', 'points':5}
print (alien_0['color']) #will output 'green'
#we can assign new key/values like any variable as well as swapping the values of a given key:
alien_0['x_pos'] = 0
alien_0['y_pos'] = 0
alien_0['color'] = "yellow"
# we can print  values by using f strings:
print(f"the alien is now {alien_0['color']}.")
#lets make the guy move

alien_0 = {"x_pos": 0, "y_pos":25, 'speed':'medium'}
# the alien moves to the right based on its speed
if alien_0['speed'] == "slow":
  x_increment = 1
elif alien_0['speed'] == 'medium':
  x_increment = 2
else:
  x_increment = 3

#new position is old position plus increment
alien_0['x_pos'] = alien_0['x_pos'] + x_increment

#key/values can also be deleted. specifying the key also removes the value
del alien_0['points']

#dictionaries can also be assigned over multiple lines like this:
favorite_languages = {
  'jen':'python',
  'markus': "javascript",
  "todd": "COBOL",
}

#we can call .title() to cap the string
language = favorite_languages['markus'].title()
print(f"Markus' favorite language is {language}")

#use get() to set a default value that will be returned if requested key doesn't exist.
# get() method requires a key as first argument and a sectond optional argument that provides the 'else' response
point_value = alien_0.get('points', 'no point value assigned.')
print(point_value)
# using get() allows for clearer answers than calling via bracket notation

