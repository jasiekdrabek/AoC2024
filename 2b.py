def is_level_good(levels):
    check = 0
    if(levels[0] > levels[1]):
        for i in range(len(levels) - 1):
            if(levels[i] > levels[i+1] and abs(levels[i] - levels[i+1]) <= 3):
                check += 1
    else:
        for i in range(len(levels) - 1):
            if(levels[i] < levels[i+1] and abs(levels[i] - levels[i+1]) <= 3):
                check += 1
    if len(levels) - 1 == check:
        return True
    return False
ans = 0
with open('2.txt', 'r') as file:
    for line in file:
        line = line[:-1]
        levels = line.split(" ")
        for i in range(len(levels)):
            levels[i] = int(levels[i])
        for i in range(len(levels)):
            if is_level_good(levels[:i] + levels[i+1:]):
                ans += 1
                break
print(ans)
