file = open("../textfiles/results.txt")
contents = file.readlines()
linenum = 0
for line in contents:
    line = line.strip("\n")
    linenum += 1
    grade = []
    if line.isalnum():
        mark = int(line)
        name1 = int(contents[linenum]) - 1
    if mark > 79:
        grade = "a"
    elif mark > 69:
        grade = "b"
    elif mark > 49:
        grade = "c"
    else:
        grade = "f"
    print(name, mark, grade)


