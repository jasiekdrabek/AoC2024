def get_valid_order(nums, graph):
    changed = True
    while changed:
        changed = False
        for i in range(len(nums)-1):
            a = nums[i]
            b = nums[i+1]
            if a in graph and b in graph[a]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                changed = True
    return nums

rules = {}
ans = 0
with open('5.txt', 'r') as file:
    for line in file:
        if(line == '\n'):
            continue
        line = line.strip()
        if 0 < len(line) <= 6:
            r,l = line.split('|')
            try:
                rules[int(r)].append(int(l))
            except KeyError:
                rules[int(r)] = [int(l)]
        else:
            updates = [int(x) for x in line.split(',')]
            changed = False
            count = False
            for i in range(len(updates)):
                if updates[i] in rules and len(updates[:i]) >= 1:
                    if len(set(updates[:i]).difference(set(rules[updates[i]]))) < len(set(updates[:i])):
                        count = True
                        changed = True
                        break
            while changed:
                changed = False
                for i in range(len(updates)-1):
                    if updates[i] in rules and updates[i+1] in rules[updates[i]]:
                        updates[i], updates[i+1] = updates[i+1], updates[i]
                        changed = True

            if count:
                ans += updates[int((len(updates))/2)]
print(ans)