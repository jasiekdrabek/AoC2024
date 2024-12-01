left = []
right = {}
ans = 0
with open('1.txt', 'r') as file:
    for line in file:
        l , r = line.split("   ")
        left.append(int(l))
        try:
            right[int(r)] += 1
        except KeyError:
            right[int(r)] = 1
for s in left:
    if s in right:
        ans +=  s * right[s]
print(ans)