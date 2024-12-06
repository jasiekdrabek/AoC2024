def find_path(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        [-1, 0], 
        [0, 1],  
        [1, 0], 
        [0, -1],
    ]
    path = []

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def find_start(grid):
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '^':
                    return i,j
    
    x,y = find_start(grid)
    current_direction = 0
    while True:
        path.append(tuple((x,y)))
        if not is_valid(x + directions[current_direction][0],y + directions[current_direction][1]):
            break
        if grid[x + directions[current_direction][0]][y + directions[current_direction][1]] == '#':
            current_direction = (current_direction + 1) % 4
        x += directions[current_direction][0]
        y += directions[current_direction][1]
    return list(set(path))
    
grid = []
with open('6.txt', 'r') as file:
    for line in file:
        line = line.strip()
        grid.append(line)

result = find_path(grid)

import sys
def pr(s):
    print(s)
sys.setrecursionlimit(10**6)
infile = '6.txt'
p2 = 0
D = open(infile).read().strip()

G = D.split('\n')
R = len(G)
C = len(G[0])
for r in range(R):
    for c in range(C):
        if G[r][c] == '^':
            sr,sc = r,c

for o_r, o_c in result:
        r,c = sr,sc
        d = 0 # 0=up, 1=right, 2=down, 3=left
        SEEN = set()
        while True:
            if (r,c,d) in SEEN:
                p2 += 1
                break
            SEEN.add((r,c,d))
            dr,dc = [(-1,0),(0,1),(1,0),(0,-1)][d]
            rr = r+dr
            cc = c+dc
            if not (0<=rr<R and 0<=cc<C):
                break
            if G[rr][cc]=='#' or rr==o_r and cc==o_c and grid[o_r][o_c] != '^':
                d = (d+1)%4
            else:
                r = rr
                c = cc
print(p2)