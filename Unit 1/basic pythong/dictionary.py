studentages = {}

studentages["Elliot"] = 16
studentages["Dave"] = 18
studentages["Paul"] = 14
studentages["Dean"] = 17

name = input("enter student name: ")

if name in studentages:
    print(studentages[name])
else:
    print("dead")

