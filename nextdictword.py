alphabets = "abcdefghijklmnopqrstuvwxyz"


#python 3
def numberingString(string):
    numbering = []
    for i in range(len(string)):
        for j in range(len(alphabets)):
            if string[i] == alphabets[j]:
                numbering.append(j)
                break
    #print(numbering)
    count = 0
    i=0
    j=0
    last = len(numbering) - 1
    for i in range(last):
        if numbering[last-i-1] < numbering[last-i]:
            pivot = numbering[last-i-1]
            for j in range(last,last-i-1,-1):
                if numbering[j] > pivot:
                    temp = numbering[j]
                    numbering[j] = pivot
                    numbering[last-i-1] = temp
                    count+=1
                    break
            tempo = []
            for j in range(last-i,last+1):
                tempo.append(numbering[j])
            for j in range(len(tempo)):
                numbering[last-i+j]= tempo[len(tempo)-j-1]
        if count == 1:
            break
   # print(numbering)
    nextword=""
    for i in range(len(numbering)):
        for j in range(len(alphabets)):
            if numbering[i] == j:
               nextword+=alphabets[j]

    if  nextword == string:
        print("no answer")
    else:
        print(nextword)
 

#n = int(input().strip())
#for i in range(n):
 #   string = input().strip()
  #  numberingString(string)
isPossible(500,5,390)

