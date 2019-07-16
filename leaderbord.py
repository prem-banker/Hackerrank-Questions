


def rankify(array):
    ranking = [] 
    for i in range(len(array)):
        ranking.append(0)
    for i in range(len(array)):
        if i==0:
            ranking[i] = 1
        elif i>=1:
            temp = array[i-1]
            rank = ranking[i-1]
            if array[i] == temp:
                ranking[i] = rank
            else:
                ranking[i] = rank + 1
    return ranking



n = int(raw_input(""))
scores = [int(scores) for scores in raw_input("").split()]
m = int(raw_input(""))
alice = [int(alice) for alice in raw_input("").split()]

alicerank = []
for element in alice:
    x = scores
    x.append(element)
    x.sort(reverse= True)
    newranks = rankify(x)
    temp = 0
    for j in range(temp,len(x)):
        if x[j] == element:       
            alicerank.append(newranks[j])
            temp = j
            break

for items in alicerank:
    print(items)
