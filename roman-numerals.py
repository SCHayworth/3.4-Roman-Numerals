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
  print('That is not a valid number.')
elif number == 1:
  print('I')
elif number == 2:
  print('II')
elif number == 3:
  print('III')
elif number == 4:
  print('IV')
elif number == 5:
  print('V')
elif number == 6:
  print('VI')
elif number == 7:
  print('VII')
elif number == 8:
  print('VIII')
elif number == 9:
  print('IX')
else:
  print('X')
