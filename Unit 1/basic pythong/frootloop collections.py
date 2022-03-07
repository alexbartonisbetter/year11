# msg = "digital sol @ sps"
# vowels = "aeiou"
#
# total = 0
#
# for i in range(len(msg)):
#     if msg[i].lower() in vowels:
#         total += 1
# print(total)


total = 0
av = 0
max = -1
min = 101
odd = 0
even = 0

nump = int(input("enetr the amount of numbers you are going to input: "))
for i in range(1,nump):
    if nump > 1:
        number = int(input("enter one of the numbers: "))
        total += number
        if number > max:
            max = number
        if number < min:
            min = number
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        av = total / number
        print(total)
        print(av)
        print(max)
        print(min)
        if odd == 1:
            print("num is odd")
        else:
            print("num is even")

    else:
        number = int(input("enter your only number loser: "))
        total = number
        max = number
        min = number
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        av = total / number
        print(total)
        print(av)
        print(max)
        print(min)
        if odd == 1:
            print("num is odd")
        else:
            print("num is even")



