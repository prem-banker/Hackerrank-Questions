import sys
#python 3
q = int(input().strip())

for i in range(q):
    n = int(input().strip())
    matrix = []
    for j in range(n):
        row = [int(row) for row in input().strip().split(' ')]
        matrix.append(row)
    
    i = 0
    j = 0
    rowsum = 0
    colsum = 0
    count = 0
    rowsum=[]
    colsum=[]
    for i in range(n):
        colsum.append(0)
        rowsum.append(sum(matrix[i]))
        for j in range(n):
            colsum[i]+=matrix[j][i]

    rowsum.sort()
    colsum.sort()
    if rowsum == colsum:
        print("Possible")
    else:
        print("Impossible")
