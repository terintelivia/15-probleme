n1 = int(input("prima nota"))
n2 = int(input("a doua nota"))
n3 = int(input("a treia nota"))
print("introdu note(numere de la 1-10)")
if n3>8:
    print(n1,n2,n3, sep=" ")
    elif n3<8:
       if n1>n2:
           print(n1)
    else:
        print(n2)
