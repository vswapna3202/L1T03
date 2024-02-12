# This program has a sentence with lots of exclamation marks 
# It replaces the exclamation mark with space using replace function
# converts the sentence to upper case using upper function and 
# reverses the string using slicing and prints all of the replaced strings to console

# Declare a sentence as per given text
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(f"{sentence}")

# Print the sentence after replace ! with space
sentence = sentence.replace("!"," ")
print(sentence)

# Print the sentence in upper case
sentence = sentence.upper();
print(sentence)

# Print the sentence in reverse using slicing
print(sentence[::-1])
