grid = []
ans = 0
zeros = []

def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

def get_to_nine(r,c,next_value):
    if not is_valid(r,c):
        return []
    if grid[r][c] != next_value:
        return []
    if grid[r][c] == 9 == next_value:
        return [(r,c)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    res = []
    for d in directions:
        res.extend(get_to_nine(r+d[0],c+d[1],next_value + 1))
    return res

with open('10.txt', 'r') as file:
    for line in file:
        line = line.strip()
        grid.append([int(l) for l in line ])
        

rows = len(grid)
cols = len(grid[0])
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            zeros.append((r,c))

for r,c in zeros:
    ans += len(set(get_to_nine(r,c,0)))
    
print(ans)