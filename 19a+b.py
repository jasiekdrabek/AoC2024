i = 0
paterns = []
designs = [] 
with open("19.txt") as file:
    for line in file:
        line = line.strip()
        if i == 0:
            paterns = line.split(', ')
            i += 1
        else:
            designs.append(line)

print(paterns)
cached = {}
def find_number_of_possible_designs(s):
    if s not in cached:
        if len(s) == 0:
            return 1
        resoult = 0
        for p in paterns:
            if s.startswith(p):
                resoult += find_number_of_possible_designs(s[len(p):])
        cached[s] = resoult
    return cached[s]

ans = 0
ans2 = 0
for d in designs:
    find_number_of_possible_designs(d)
for d in designs:
    if not d in cached:
        continue
    if cached[d] > 0:
        ans +=1
        ans2 += cached[d]
        
print(ans)
print(ans2)        