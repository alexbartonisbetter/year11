# for i in range(5,37,3):
#     print(i)

#-----------------------------------------------------------------------------------

# input = int(input("enter the number you want to to know the times table for: "))
#
# for i in range(1, 13):
#     print(i * input)

#-----------------------------------------------------------------------------------

# n1 = int(input("enter ur first n: "))
# n2 = int(input("enter ur second n: "))
#
# total = 0
#
# for x in range(n1, n2+1, 1):
#     total += x
#
# print(total)

#-----------------------------------------------------------------------------------

# for x in range (1, 51):
#     if x % 7 == 0:
#         print(x)

# -----------------------------------------------------------------------------------

# import random
#
# for i in range(5):
#     num = random.randint(1, 6)
#     print(num)

#-----------------------------------------------------------------------------------

# roll_total = 0
# import random
# rolls = int(input("enter the amount of times you want to roll a dice: "))
#
# for i in range(1,rolls):
#     roll_count = rolls
#     rollnum = random.randint(1, 6)
#     roll_total += rollnum
#     total = roll_total
#     print("roll number ", roll_count,

#-----------------------------------------------------------------------------------

# import random
# amount = int(input("how many rolls: "))
# for i in range(1, amount):
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     amount2 = dice1 + dice2
#     if amount2 == 7:
#         print("7, you win")
#     else:
#         print(amount2, "you lose")

#-----------------------------------------------------------------------------------

# user_input = int(input("pick a number: "))
#
# fcount = 0
#
# for i in range(2, user_input + 1):
#     if user_input % i == 0:
#         print(i)
#         fcount += 1
# if fcount > 1:
#     print(user_input, "isnt prime")
# else:
#     print(user_input, "is prime")

#-----------------------------------------------------------------------------------

#1
#22
#333
#4444
#55555


# for num in range(6):
#     value = ""
#     if int(num) > 0:
#         for i in range(num-1):
#             value = value + str(num)
#         print(value + str(num))

# for char in range (1,6):
#     value = ""
#     for i in range(char-1):
#         value = value + str("_")
#     print(value + "#")

# A
# B B
# C C C
# D D D D
# E E E E E

# for num in range(6):
#     value = ""
#     if int(num) == 1:
#         value2 = "A"
#     if int(num) == 2:
#         value2 = "B"
#     if int(num) == 3:
#         value2 = "C"
#     if int(num) == 4:
#         value2 = "D"
#     if int(num) == 5:
#         value2 = "E"
#     for i in range(num):
#         value += str(value2)
#     print(value)

# 1
# 23
# 345
# 4567
# 56789
#
# numbers = "123456"
#
# for num in range(len(numbers)):
#     value = ""
#     if int(num) > 0:
#         for i in range(0, num):
#             value += num
#         print(value)

#--------------------------------------------------------------

n = int(input("Enter max number: "))
for i in range(1, n+1):
    sum = 0
    factors = ""
    for x in range(1, i):
        if(i % x == 0):
            sum = sum + i
            factors = factors + str(x) + " "
    if (sum == i):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")