def checkDiagonals(x,y,arr1,arr2,n):
    topright = min(n-x,n-y)
    topleft = min(n-x,y-1)
    bottomleft = min(y-1,x-1)
    bottomright = min(n-y,x-1)
    for i in range(len(arr1)):
        xdis = arr1[i]-x
        ydis = arr2[i] -y
        if  xdis == ydis and xdis > 0 and xdis < topright:
            topright = xdis - 1
            
        elif xdis == -1*ydis and xdis > 0 and xdis < topleft:
            topleft = xdis - 1
            
        elif xdis == ydis and xdis < 0 and xdis < bottomleft:
            bottomleft = -1*xdis - 1
            
        elif xdis == -1*ydis and xdis < 0 and xdis < bottomright:
            bottomright = -1*xdis - 1
    diagonal = topright + topleft + bottomright + bottomleft
    
    return diagonal

def checkSides(x,y,arr1,arr2,n):
    top = n-x   #1
    bottom = x-1#3== 1
    left = y-1#2 == 0 
    right = n - y #2
    for i in range(len(arr1)):
        xdis = arr1[i]-x#1
        ydis = arr2[i] -y
        
        if x == arr1[i] and ydis <= 0 and -1*ydis < left:
            if ydis == -1:
                left = 0
            else :    
                left = -1*ydis -1
                
        elif x == arr1[i] and 0 < ydis < right:
            if ydis == 1 :
                right = 0
            else :    
                right = ydis - 1
                
        elif y == arr2[i] and xdis <= 0 and -1*xdis < bottom :
            if xdis == -1 :
                bottom = 0
            else :    
                bottom = -1*xdis - 1
               
        elif y == arr2[i] and 0 < xdis < top:
            if xdis == 1 :
                top = 0
            else :   
                top = xdis - 1
               
        
    sides = top + bottom + left + right
    return sides
    
obstaclerow = []
obstaclecolumn = []

n,k = raw_input("").split()
queenrow,queencolumn = raw_input("").split()
for i in range(int(k)):
    r,c = raw_input("").split()
    obstaclerow.append(int(r))
    obstaclecolumn.append(int(c))
    


ans1 =checkDiagonals(int(queenrow),int(queencolumn),obstaclerow,obstaclecolumn,int(n))
ans2 =checkSides(int(queenrow),int(queencolumn),obstaclerow,obstaclecolumn,int(n))    
print(ans1 + ans2)        









