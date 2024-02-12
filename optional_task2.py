# This program takes in a string with users favourite restaurant name and also his favourite number
# and displays it.

# Get favourite restaurant name from user and assign it to string_fav
string_fav = input("Enter your favourite restaurant name: ")

# Get favourite number from user and assign it to int_fav
int_fav = int(input("Enter your favourite number: "))

# Print string_fav to the console
print("Your favourite restaurant is {}".format(string_fav))

# Print int_fav to the console
print(f"Your favourite number is {int_fav}")

# Try casting string_fav which is a string as an integer
# When this code was run obtained an error "Invalid literal  for int() with base 10: <name>"
# as casting for int expects an integer but which is stored as string. 
# string_fav does not hold number as string, it holds a name which cannot be converted to integer.
#new_int = int(string_fav)