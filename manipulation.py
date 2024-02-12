# This program accepts a sentence from the user and manipulates it using different
# functions and slicing

# Input the sentence from the user and assign it to variable str_manip
str_manip = input("Enter a sentence: ")

# Get the length of sentence str_manip by using len function and print it
str_len = len(str_manip)
print(str_len)

#Get the last letter in the sentence and replace all the last letters in it with "@"
str_last_letter = str_manip[str_len-1:str_len]
print(str_manip.replace(str_last_letter,"@"))

#Get the last 3 letters in the sentence and print it in reverse
str_last_three = str_manip[str_len-3:str_len]
print(str_last_three[::-1])

#Get the first 3 letters and last 2 letters of the sentence and print it as one string
str_new = str_manip[0:3]
str_new = str_new + str_manip[str_len-2:str_len]
print(str_new)
