xa = int(input("numarul de bile albe mici"))
xr = int(input("numarul de bile rosii mici"))
xv = int(input("numarul de bile verzi mici"))
ya = int(input("numarul de bile albe mari"))
yr = int(input("numarul de bile rosii mari"))
yv = int(input("numarul de bile verzi mari"))
xt = xa+xr+xv
yt = ya+yr+yv
print("in total=",xt+yt, "bile")
if xt>yt:
    print("bile mici sunt mai multe")
if yt>xt:
    print("bile mari sunt mai multe")
if xt=yt:
    print("numarul de bile mici si numarul de bile mari sunt egale")
if ((xa+ya>xr+yr) and (xa+ya>xv+yv)):
    print("bile albe:",xa+ya)
if ((xr+yr>xa+ya) and (xr+yr>xv+yv)):
    print("bile albe:",xr+yr)
if ((xv+yv>xa+ya) and (xv+yv>xr+yr)):
    print("bile albe:",xv+yv)
if ((xa+ya==xr+yr) and (xr+yr>xv+yv)):
    print("bile rosii:",xa+ya)
if ((xr+yr==xv+yv) and (xr+yr>xa+ya)):
    print("numarul de bile rosii si numarul de bile verzi sunt egale:",xr+yr)
if((xa+ya==xv+yv) and (xa+ya>xr+yr)):
    print("numarul de bile albe si de bile rosii sunt egale:",xa+ya)
else:
    print("numarul de bile albe,bile rosii si bile verzi sunt egale:",xa+ya)