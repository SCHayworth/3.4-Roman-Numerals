# 3-4 Roman Numerals
# Shaun Hayworth
# CIS 2
# 10-02-2019

# Gets an integer between 1 and 10 from the user, and displays the corresponding Roman numeral. Displays an error message
# if the supplied number is ouside the 1-10 range.

# Prompt user for a number between 1 and 10 and store it in the number variable.
number = int(input('Please enter a number between 1 and 10: '))

# Determine whether or not the number is within the specifid range. If so, print the appropriate Roman numeral
if number < 1 or number > 10:
  print('\nThat is not a valid number.')
elif number == 1:
  print('\nI')
elif number == 2:
  print('\nII')
elif number == 3:
  print('\nIII')
elif number == 4:
  print('IV')
elif number == 5:
  print('\nV')
elif number == 6:
  print('\nVI')
elif number == 7:
  print('\nVII')
elif number == 8:
  print('\nVIII')
elif number == 9:
  print('\nIX')
else:
  print('\nX')
