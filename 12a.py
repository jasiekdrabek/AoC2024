def get_area(r,c):
    if (r,c) in visited:
        return 0
    visited_area.add((r,c))
    visited.add((r,c))
    if is_valid(r + 1,c):
                if gardens[r + 1][c] == gardens[r][c] and (r + 1,c) not in visited:
                    get_area(r+1,c)
    if is_valid(r,c + 1):
                if gardens[r][c + 1] == gardens[r][c] and (r,c + 1) not in visited:
                    get_area(r,c+1)
    if is_valid(r - 1,c):
                if gardens[r - 1][c] == gardens[r][c] and (r - 1,c) not in visited:
                    get_area(r-1,c)
    if is_valid(r,c - 1):
                if gardens[r][c - 1] == gardens[r][c] and (r,c - 1) not in visited:
                    get_area(r,c-1)
    return len(visited_area)

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

gardens = []
with open('12.txt', 'r') as file:
    for line in file:
        line = line.strip()
        gardens.append([l for l in line ])

rows = len(gardens)
cols = len(gardens[0])
visited = set()
areas = []
parameters = []

for r in range(rows):
    for c in range(cols):
        parameter = 0
        visited_area = set()
        area = get_area(r,c)
        if len(visited_area) != 0:
            for x,y in visited_area:
                parameter += 4
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for d in directions:
                    if is_valid(x + d[0], y + d[1]):
                        if gardens[x + d[0]][y + d[1]] == gardens[x][y]:
                            parameter -= 1    
            areas.append(area)
            parameters.append(parameter)       
ans = 0
for i in range(len(areas)):
    ans += areas[i] * parameters[i]

print(ans)