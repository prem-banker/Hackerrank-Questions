    len1 = len(string1)
    len2 = len(string2)
    x = k
    count = 0
    for i in range(min(len1,len2))
        if string1[i] != string2[i] :
            if k < len1 + len2 :
                print("No")
                return
            elif k == len1 + len2:
                print("Yes")
                return
            elif k > len1 + len2:
                print("Yes")
                return
        else:
            k-=1
            len1-=1
            len2-=1
    if len1 > len2 : #prembank prem
        for i in range(len2):
            if string1[i] == string2[i]:
                count+=1
            elif string1[i] != string2[i] :
                if k < len1 + len2 :
                    print("No")
                    return
                elif k == len1 + len2:
                    print("Yes")
                    return
                elif k > len1 + len2:
                    print("Yes")
                    return                
