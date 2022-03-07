def check_luhn(card_num):
    num_digits = len(card_num)
    num_sum = 0
    is_second = False
    for i in range(num_digits - 1, -1, -1):
        d = ord(card_num[i]) - ord('0')
        if is_second == True:
            d = d * 2
        num_sum += d // 10
        num_sum += d % 10
        is_second = not is_second
    if num_sum % 10 == 0:
        return True
    else:
        return False


data = open("../textfiles/luhn")
data = data.readlines()
contents = data
for line in contents:
    line = line.strip("\n")
    line = line.strip(" ")
    line = line.strip("E")
    line = line.strip("V")
    if check_luhn(line):
        print("This is valid")
    else:
        print("This is not valid")