current_number = 1
while current_number <= 5:
  print(current_number)
  current_number += 1

prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
  message = input(prompt)
  print(message)

#this program will constantly spit back the user input, terminating the while... loop only on the given quit
# adding this next block makes it so tthat it doesn't return 'quit' and just quits. (replacing 11 & 12)

if message != "quit":
  print(message)

#we can also add flags that will monitor whether or not the program should continue to run:
active = True
while active:
  message = input(prompt)

  if message =='quit':
    active = False
  else:
    print(message)

#this is the same output as previous, but we could theoretically add more tests to determine the desired outputs, or other
#  conditions where we want active to switch to false

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd loveto go to {city.title()}")

# this loop will continue forever until the user 'quit's 

#instead of choosing a quit, we can tell it to continue

current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue

  print(current_number)

# this goes through 10 times and, if the # is even, skip the rest of the code & return to start
#so output will be 1, 3, 5, 7, 9

#be careful to add an exit to your loop, lest ye be caught forever in its grasp.
# if we omit ln 50, we'll forever print 1's . It doesn't hurt to test it out
# a little bit at a time, scrutinizing the conditions.

#looping through dictionaries and lists

# start with users that need verification and an empty list of verified users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#verify and add into confirmed list
while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"verifying user: {current_user.title()}")
  confirmed_users.append(current_user)

  print("\n the followign users have been confirmed")
  for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# we can also remove all instances of specific values from a list
pets = ['cat', 'dog','godlfish','cat','rabbit','cat']

while 'cat' in pets:
  pets.remove('cat')

print(pets)

# filling a dictionary with user inputs:
# create an empty dictionary
responses = {}
# set an active flag & active conditionals
polling_active = True
while polling_active:
  name = input("\nWhat is your name?")
  response = input("Which mountain waould you like to climb someday?")
  #set responses[key name] to value
  responses[name] = response
  repeat = input("would you like to let another person respond? (yes/no)")
  if repeat == 'no':
    polling_active = False
#once active is set to false
print("\n -- Poll Results --")
for name, response in responses.items():
  print(f"{name} would like to climb {response}")
