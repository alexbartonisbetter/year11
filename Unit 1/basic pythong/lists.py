# import random
#
# balls = []
#
# for num in range(6):
#     ball = int(random.randint(1,45))
#     while ball in balls:
#         ball = int(random.randint(1, 45))
#     balls.append(ball)
#
# balls.sort()
# print(balls)

# input = input("english: ")
# words = input.split(" ")
# piglatin = ""
#
# for word in words:
#     newword = word
#     if len(word) == 1:
#         latin_word = (newword + "ay")
#     else:
#         latin_word = newword[1:] + newword[0] + "ay"
#     piglatin = piglatin + latin_word + " "
# print(piglatin)


cd_msg = input("input coded message: ")
cl_msg = ""
words = cd_msg.split(" ")
words.reverse()
for word in words:
    if word[0] is