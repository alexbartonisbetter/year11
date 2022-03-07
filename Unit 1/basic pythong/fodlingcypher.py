#II REOA LAI NYWLRVMD

def split(word):
    return [char for char in word]

list1 = []
sol = []
contents = []
cipher = "II*REOA*LAI*NYWLRVMD"
cipher = [split(cipher)]
for x in cipher:
    print(x)
    while len(sol) < len(list1):
        sol += contents
        print(sol)
