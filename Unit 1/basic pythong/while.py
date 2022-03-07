# x = 10
# while x > 0:
#     print(x)
#     x = x - 1
# print("blast off")

# msg = "Hello World"
# x = 0
# while x < 11:
#     print(msg[x])
#     x += 1

# w = 0
# while w % 10 != 2:
#     w = (w + 4) % 2
#     print("w=", int(w))

# name = input("whats your name contestant: ")
# while name != "QUIT":
#     print(name)
#     name = input("whats your name contestant: ")

#----------------------------------------------------------------

# b = 1
# n = int(input("number: "))
# while n > 0:
#     b = n
#     n = n - 1
#     c = n * b
#     print(c)

# number = int(input("Enter number:"))
# factorial = 1
# while number>0:
#     factorial = factorial * number
#     number = number - 1
# print(factorial)

year = 0
upop = 26000000
while upop < 50000000:
    upop = upop * 1.03
    year += 1
print(year)

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))
result = num1 % num2
while result:
    num1 = num2
    num2 = result
    result = num1 % num2
print('GCD is:', num2)