import math

x1,v1,x2,v2 = raw_input("").split()

x1 = int(x1)
v1 = int(v1)
x2 = int(x2)
v2 = int(v2)


if x1 > x2 and v1 > v2:
    print("NO")
elif x2 > x1 and v2 > v1 :
    print("NO")
elif x1 > x2 and v1 < v2 :
    if (x1 - x2)%(v2 - v1) == 0:
        print("YES")
    else:
        print("NO")
elif x2 > x1 and v1 > v2 :   
    if  (x2 - x1)%(v1 - v2) == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
        
        
