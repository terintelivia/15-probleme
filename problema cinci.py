ac = int(input("anul curent"))
lc = int(input("luna curenta"))
zc = int(input("ziua curenta"))
an = int(input("anul nasterii"))
ln = int(input("luna nasterii"))
zn = int(input("ziua nasterii"))
if ln>lc:
    print((ac-an)+1, "ani")
    else:
        print(ac-an, "ani")