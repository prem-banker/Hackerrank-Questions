import math

n,h = raw_input("").split()

wallpoints = [int(wallpoints) for wallpoints in raw_input("").split()]
length = [int(length) for length in raw_input("").split()]

n = int(n)
h = int(h)

if len(wallpoints) != n or len(length) != n:
    print("error")
    
ladder = []
for i in range(len(length)) :
    ladder.append(math.ceil(wallpoints[i] - 0.25*length[i]-h))

if max(ladder) >=0 :
    print max(ladder)    
elif max(ladder) < 0 :
    print 0
