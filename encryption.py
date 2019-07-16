import math

string = raw_input()
rows = math.floor(math.sqrt(len(string)))
columns = math.ceil(math.sqrt(len(string)))

encrypt = []

for i in range(int(rows)+1):
    encrypt.append("")
    
for i in range(int(rows)+1):
    for j in range(len(string)):
        if i == j%columns:
            encrypt[i]+=string[j]
output = ""
for items in encrypt :
    output+= items + " "
            
print(output)
