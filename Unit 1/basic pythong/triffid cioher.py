import sys
sys.stdout = open('../textfiles/triffid log alphabet', 'w')

def table(i):
    alph = list("abcdefghijklmnopqrstuvwxyz ")
    decodic = {}
    i = list(i)
    count = 0
    multiple = 0
    multinc = 0
    for char in i:
        count += 1
        print("count 1", count)
        if count > 3:
            count = 1
            print("count 2", count)
            multiple += 1
            print("multiple 1", multiple)
        if multiple > 2:
            multiple = 0
            print("multiple 2", multiple)
            multinc += 1
            print("multinc", multinc)
        if char in alph:
            decodic[char] = 110 + count + (multiple * 10) + multinc * 100
            assert isinstance(char, object)
            alph.remove(char)
    if len(alph) != 0:
        for char in alph:
            count += 1
            print("count 1", count)
            if count > 3:
                count = 1
                print("count 2", count)
                multiple += 1
                print("multiple 1", multiple)
            if multiple > 2:
                multiple = 0
                print("multiple 2", multiple)
                multinc += 1
                print("multinc", multinc)
            if char in alph:
                decodic[char] = 110 + count + (multiple * 10) + multinc * 100
                alph[char].remove()
    return decodic


decodekey = input("key: ")
decodekey = decodekey.lower()
for i in range(1):
    x = table(decodekey)
    print(x)

sys.stdout.close()