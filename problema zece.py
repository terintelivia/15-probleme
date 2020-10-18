ng = int(input("dati numarul de gaini"))
nc = int(input("dati numarul de curcani"))
nb = int(input("dati numarul total de boabe"))
nbg = int(input("numarul de boabe pentru gaini"))
nbc = int(input("numarul de boabe pentru curcan"))
ng =10
nc =20
nbg = nb//ng
nbc = nb-(ng*nbg)
if nbg>nbc:
    print("gaina primeste mai mult cu=",nbg-nbc, "boabe")
elif nbc>nbg:
    print("curcacul primeste mai mult cu=",nbc-nbg, "boabe")
else:
    print("ambii primesc acelasi numar de boabe")