n = int(raw_input())
scores = [int(scores) for scores in raw_input().split(" ")]

min = 0
max = 0
minnumber = scores[0]
maxnumber = scores[0]
for i in range(1,len(scores)):
    if scores[i] < minnumber :
        min+=1
        minnumber = scores[i]
    elif scores[i] > maxnumber:
        max+=1
        maxnumber = scores[i]

print(str(max)+ " " + str(min))
