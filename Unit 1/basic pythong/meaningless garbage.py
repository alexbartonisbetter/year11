import string
dicalpha = dict.fromkeys(string.ascii_lowercase, 0)
dicalphatotal = 0
notinclusive = ""
importdata = open("../textfiles/pangrams")
contents = importdata.readlines()
for line in contents:
    line = line.lower()
    line = list(line)
    for x in line:
        if x in dicalpha:
            dicalpha[x] += 1
            dicalphatotal += 1
        if dicalphatotal < len(line):
            print("not panagram")
            for k, v in dicalpha:
                if v == 0:
                    notinclusive += (v + ", ")
            print("missing:", notinclusive)
        else:
            print("is pangram")