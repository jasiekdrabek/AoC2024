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
            good_updates = 0
            for i in range(len(updates)):
                if updates[i] in rules and len(updates[:i]) >= 1:
                    if len(set(updates[:i]).difference(set(rules[updates[i]]))) < len(set(updates[:i])):
                        break
                good_updates += 1
            if good_updates == len(updates):
                ans += updates[int((len(updates))/2)]
print(ans)