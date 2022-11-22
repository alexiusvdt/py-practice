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

