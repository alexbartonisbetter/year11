def isomorph(a):
    iso = ''
    var = 0
    for char in a:
        var += 1
        run = True
        for num in range(var, len(a)):
            if run is True:
                if a[num] == char:
                    iso += " +" + str(num - var + 1)
                    run = False
        if run is True:
            iso += " " + str(0)
    return iso


data = open("text").readlines()
for words in data:
    words = words.strip('\n')
    wrd_1, wrd_2 = words.split()
    iso_1 = isomorph(wrd_1)
    iso_2 = isomorph(wrd_2)
    if len(wrd_1) == len(wrd_2):
        if iso_1 == iso_2:
            print(wrd_1 + ",", wrd_2, "are isomorphs with the repetition pattern" + iso_1)
        else:
            print(wrd_1 + ",", wrd_2, "are not isomorphs")
    else:
        print(wrd_1 + ",", wrd_2, "have different lengths")