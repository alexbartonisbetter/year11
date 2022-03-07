#
# loop = True
# while loop is True:
#     age = input("how old are you? ").strip( )
#     if str.isdigit(age):
#         age = int(age)
#         if age >= 18 and age == is_int():
#             print("buy alcohol")
#         else:
#             print("dont buy alcohol dropkcik")
#     else:
#         print("thats not a number dipshit")

#--------------------------------------------------------------

# digits = input("enter your numbers: ").strip()
# if str.isdigit(digits):
#     total = 0
#     for d in digits:
#         total = total +int(d)
#     print(total)
# else:
#     print("only numbers")

#-------------------------------------------------------------

# total_earnt = 1
# shirt_price = 100
# shirt_total_price = 1
# shirt_total = input("how many shirts did you sell?: ")
#
# if str.isdigit(shirt_total):
#     shirt_total_price = shirt_total * shirt_price
#     shirt_total_price = int(shirt_total_price)
#     print("You sold", shirt_total_price, "worth of shirts")
#     if shirt_total_price >= 10000:
#         total_earnt = shirt_total_price * 0.1
#     else:
#         total_earnt = shirt_total_price * 0.05
#     print("You have earnt", total_earnt)
# else:
#     print("tye a number")

#-------------------------------------------------------------

# word = input("write it nerd: ").strip()
# wordhalf = len(word) / 2
# if (len(word) % 2) == 0: print("its even", "first part is", word[:int(wordhalf)], "the second part is", word[int(wordhalf):])
# else: print("its odd", "the middle is", word[int(wordhalf):int(wordhalf+1)])

#-------------------------------------------------------------

no_digits = True
text = False
correct = 0

special_chars = "`~!@#$%^&*()-_=+?><:;'"

loop = True
while loop == True:
    user_input = input("make a new password: ").strip()
    if len(user_input) <= 5:
        print("password must be longer")
    elif len(user_input) > 21:
        print("password too long")
    if any(c in special_chars for c in user_input):
        print("you have special characters")
        correct += 1
    else:
        print("no spec chars")
    for character in user_input:
        if character.islower():
            text = True
        if character.isupper():
            text = True
        if character.isdigit():
            no_digits = False
            loop = False
    if no_digits:
        print("no digits")
    if text is False:
        print("no characters")
    if no_digits is False:
        print("you have a digit")
        correct += 1
    if correct == 2:
        print("your password has been accepted")

#-----------------------------------------------------------------------








