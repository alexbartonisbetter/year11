import random
filename = "../textfiles/quotes.txt"

file = open(filename)

contents = file.readlines()
# print(type(contents))
# print(contents)

quote = random.choice(contents).strip("\n")

print(quote)