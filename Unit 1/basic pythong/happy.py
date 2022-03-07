def happy(n):
    number = str(n)
    container = []
    while True:
        temp = 0
        for digit in number:
            temp += int(digit) ** 2
        if temp == 1:
            return True
        elif temp in container:
            return False
        else:
            container.append(temp)
            number = str(temp)


count = 0
for i in range(1, 1001):
    if happy(i):
        count += 1
print("Total happy numbers below 1000: " + str(count))