data = open("../textfiles/data")
data = list(data)
newdata = []
for i in data:
    newdata.append(i.split('\n')[0])
for line in newdata:
    data_line = list(line)
    for n in data_line:
        n = int(n)
        if n > 9:
            n = n - 9
        else:
            n += n
            if n > 9:
                n = n - 9
        total = n
    print(total)