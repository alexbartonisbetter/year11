person = []
name = ''
mark = ''
average = ''
file = open("../textfiles/studentdata.txt")
contents = file.readlines()
for line in contents:
    line = line.strip("\n")
    person += line.split(" ")
    for i in person:
        if i.isalltext:
            person.pop(i)
    mark = len(person)



    name += person[0]
    person = person[1:]