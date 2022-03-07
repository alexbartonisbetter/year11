def iso(a, b):
    worda = a
    wordb = b
    a = list(a)
    b = list(b)
    iso_a = ''
    iso_b = ''
    count = 0
    count2 = 0
    append_store_a = ''
    append_store_b = ''
    for char in a:
        if a.count(char) > 1:
            for char2 in a:
                if char2 == char:
                    append_store_a = str(char2)
                elif char2 != char:
                    count += 1
    for char in a:
        if char == append_store_a:
            append_store_a = ''
            iso_a += ' ' + str(count - 1)
            count = 0
        else:
            iso_a += ' 0'

    for char in b:
        if b.count(char) > 1:
            count2 = 0
            for char2 in b:
                if char2 == char:
                    append_store_b = str(char2)
                elif char2 != char:
                    count2 += 1
    for char in b:
        if char == append_store_b:
            append_store_b = ''
            iso_b += ' ' + str(count2 - 1)
            count2 = 0
        else:
            iso_b += ' 0'

    if len(a) != len(b) and iso_a != iso_b:
        return False
    if iso_a == iso_b:
        print(worda, "and", wordb, "are isomorphs with", iso_b, iso_a, "as the pattern")



data = open('text')
data = data.readlines()
for line in data:
    word = line.split()
    iso(str(word[0]), str(word[1]))