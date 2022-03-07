data = open("text")
data = data.readlines()
for words in data:
    wrd_1, wrd_2 = words.split()
    iso_1 = ''
    iso_2 = ''
    var_1 = 0
    var_2 = 0
    for char in wrd_1:
        var_1 += 1
        run_1 = True
        for num in range(var_1, len(wrd_1)):
            if run_1 is True:
                if wrd_1[num] == char:
                    iso_1 += " +" + str(num - var_1 + 1)
                    run_1 = False
        if run_1 is True:
            iso_1 += " " + str(0)
    for char in wrd_2:
        var_2 += 1
        run_2 = True
        for num in range(var_2, len(wrd_2)):
            if run_2 is True:
                if wrd_2[num] == char:
                    iso_2 += " +" + str(num - var_2 + 1)
                    run_2 = False
        if run_2 is True:
            iso_2 += " " + str(0)
    if len(iso_1) == len(iso_2):
        if iso_1 == iso_2:
            print(wrd_1 + ",", wrd_2, "are isomorphs with the repetition pattern" + iso_1)
    elif iso_1.count("+") != iso_2.count("+"):
        print(wrd_1 + ",", wrd_2, "are not isomorphs")
    else:
        print(wrd_1 + ",", wrd_2, "have different lengths")