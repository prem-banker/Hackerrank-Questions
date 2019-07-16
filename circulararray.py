def circularArrayRotation(array,k):
    temp =[]
    for i in range(len(array)):
        temp.append(array[(i-k)%len(array)])

    return temp

n,k,q = raw_input().split(" ")
array = [int(array) for array in raw_input().split(" ")]
#ans = circularArrayRotation(array,int(k))
for i in range(int(q)):
    q = int(raw_input())
    print(array[(q-int(k))%int(len(array))])
    
