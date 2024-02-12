# This program gets three integers from the user and does various calculations on it

# Get first integer and assign it to first_number after casting it to int
first_number = int(input("Enter Integer1: "))

# Get second integer and assign it to second_number after casting it to int
second_number = int(input("Enter Integer2: "))

# Get third integer and assign it to third_number after casting it to int
third_number = int(input("Enter Integer3: "))

# Calculate sum of all the integers and print it to the console
print("Sum of all numbers is: {}".format(first_number + second_number + third_number))

#Calculate first integer minus the second integer and print it to the console
print("First minus second number is: {}".format(first_number-second_number))

#Calculate the third integer multiplied by first integer and print it to console
print("Third multiplied by first number is: {}".format(third_number*first_number))

#Calculate sum of all the integers and divide it by the third number and print it to console
print("Sum of all numbers divided by third number is: {}".format((first_number + second_number + third_number)/third_number))