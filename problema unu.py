n1 = int(input("dati date de intrare:"))
n2 = int(input("dati date de intrare:"))
n3 = int(input("dati date de intrare:"))
p1 = int(input("dati date de intrare:"))
p2 = int(input("dati date de intrare:"))
p3 = int(input("dati date de intrare:"))
if (p1>p2) and (p1>p3):
    print(n1)
if (p2>p1) and (p2>p3):
    print(n2)
if (p3>p1) and (p3>p2):
    print(n3)
if (p1==p2) and (p1>p3) and (p2>p3):
    print(n1 and n2 , "acelasi punctaj")
if (p1==p2) and (p1>p2) and (p3>p2):
    print(n1 and n3)
