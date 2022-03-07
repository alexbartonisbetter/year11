def checkDivisibility(n, digit):
    return digit != 0 and n % digit == 0


def allDigitsDivide(n):
    temp = n
    while temp > 0:
        digit = temp % 10
        if not checkDivisibility(n, digit):
            return False
        temp = temp // 10
    return True


n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
total = 0

for x in range(n1, n2):
    if allDigitsDivide(x):
        total += 1
print(total)
