def isPossible(cap1, cap2 , ans):
    a = cap1
    b = 0
    count = 0
    while ( count==0 ):
       # print(a,b)
        if a > cap2 and b == 0:
            a = a-cap2
            b = min(cap2,b+cap2)
            if a == ans or b == ans:
                print("YES")
                count+=1
            b = 0
        elif 0 < a < cap2 and b == 0:
            b = min(cap2, b+a)
            a = 0
            if a == ans or b == ans:
               print("YES")
               count+=1
            a = cap1
        elif a == cap1 and 0 < b < cap2:
            temp = cap2 - b
            b = b + temp
            a = a - temp
            if a == ans or b == ans:
               print("YES")
               count+=1
            b = 0
        else :
            print("NO")
            count+=1


testcases = int(raw_input())
for i in range(testcases):
    x,y,ans = raw_input().split(" ")
    if int(x) >= int(y):
        isPossible(int(x),int(y),int(ans))
    else:
        isPossible(int(y),int(x),int(ans))
    
        

