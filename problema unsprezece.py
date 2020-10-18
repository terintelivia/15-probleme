a = int(input("dati primul numar"))
b = int(input("dati al doilea numar"))
c = int(input("dati al treilea numar"))
if ((a%2==0) and (b%2==0) and (c%2==0)):
    print(a," numar par")
    print(b,"numar par")
    print(c,"numar impar")
elif ((a%2==0) and (b%2==0) and (c%2!=0)):
    print(a,"numar par")
    print(b,"numar par")
    print(c,"numar impar")
elif ((a%2==0) and (b%2!=0) and (c%2==0)):
    print(a,"numar par")
    print(b,"numar impar")
    print(c,"numar par")
elif ((a%2!=0) and (b%2==0) and (c%2==0)):
    print(a,"numar impar")
    print(b,"numar par")
    print(c,"numar par")
elif ((a%2!=0) and (b%2!=0) and (c%2==0)):
    print(a,"numar impar")
    print(b,"numar impar")
    print(c,"numar par")
elif ((a%2!=0) and (b%2==0) and (c%2!=0)):
    print(a,"numar impar")
    print(b,"numar par")
    print(c,"numar impar")
elif ((a%2==0) and (b%2!=0) and (c%2!=0)):
    print(a,"numar par") 
    print(b,"numar impar")
    print(c,"numar impar")
else:
    print(a,"numar impar")
    print(b,"numar impar")
    print(c,"numar impar")