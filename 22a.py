with open("22.txt") as fin:
    lines = fin.read().strip().split("\n")
    
ans = 0

for line in lines:
    line = int(line)
    for i in range(2000):
        line = ((line * 64) ^ line) % 16777216
        line = ((line // 32) ^ line) % 16777216
        line = ((line * 2048) ^ line) % 16777216
    ans += line
print(ans)
        