left = []
right = []
ans = 0
with open('1.txt', 'r') as file:
    for line in file:
        l , r = line.split("   ")
        left.append(int(l))
        right.append(int(r))
left.sort()
right.sort()
for i in range(len(right)):
    ans += abs(left[i] - right[i])
print(ans)
