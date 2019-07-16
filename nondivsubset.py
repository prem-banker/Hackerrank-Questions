






'''
ans = []
maxi = []
count = 0

for num1 in s:
    ans.append(num1)
    #print("num1 : "+ str(num1))
    for num2 in s:
        #print("num2 + " + str(num2))
        if (num1+num2)% int(k) !=0 and num1 != num2 :
            for num in ans:
                #print(ans)
                if (num+num2)%int(k) != 0 and num!=num2:
                    count+=1
                else:
                    count+=0
                
            if count == len(ans):
                ans.append(num2)
                count= 0
    maxi.append(len(ans))
    #print(maxi)
    #print(ans)
    ans = []

print(max(maxi))    

'''             
