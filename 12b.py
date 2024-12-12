def get_area(r,c,visited,visited_area):
    if (r,c) in visited:
        return 0
    visited_area.add((r,c))
    visited.add((r,c))
    if is_valid(r + 1,c):
                if gardens[r + 1][c] == gardens[r][c] and (r + 1,c) not in visited:
                    get_area(r+1,c,visited,visited_area)
    if is_valid(r,c + 1):
                if gardens[r][c + 1] == gardens[r][c] and (r,c + 1) not in visited:
                    get_area(r,c+1,visited,visited_area)
    if is_valid(r - 1,c):
                if gardens[r - 1][c] == gardens[r][c] and (r - 1,c) not in visited:
                    get_area(r-1,c,visited,visited_area)
    if is_valid(r,c - 1):
                if gardens[r][c - 1] == gardens[r][c] and (r,c - 1) not in visited:
                    get_area(r,c-1,visited,visited_area)
    return len(visited_area)

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def get_sides(visited_area):
    edges_set = set()
    side = 0
    for x,y in visited_area:
        directions = [[1,0,'DOWN'],[0,1,'LEFT'],[-1,0,'UP'],[0,-1,'RIGHT']]
        for d in directions:
            if is_valid(x + d[0], y + d[1]):
                if gardens[x + d[0]][y + d[1]] != gardens[x][y]:
                    edges_set.add((x,y,d[2]))
            else:    
                edges_set.add((x,y,d[2]))
    edges_list = list(edges_set)
    edges_list = sorted(edges_set, key=lambda tup: (tup[0],tup[1],tup[2]) )
    current_edge = edges_list[0]
    while len(edges_list) > 0:
        edges_list.remove(current_edge)
        if (current_edge[0] + 1,current_edge[1],current_edge[2]) in edges_set:
            current_edge = (current_edge[0] + 1,current_edge[1],current_edge[2])
        elif (current_edge[0],current_edge[1] + 1,current_edge[2]) in edges_set:
            current_edge = (current_edge[0],current_edge[1]+1,current_edge[2])
        else:
            side += 1
            if len(edges_list) > 0:
                current_edge = edges_list[0]
    return side
            
gardens = []
with open('12.txt', 'r') as file:
    for line in file:
        line = line.strip()
        gardens.append([l for l in line ])

rows = len(gardens)
cols = len(gardens[0])
visited = set()
areas = []
sides = []

for r in range(rows):
    for c in range(cols):
        visited_area = set()
        area = get_area(r,c,visited,visited_area)
        if area != 0:
            side = get_sides(visited_area)
            areas.append(area)
            sides.append(side)
                   
ans = 0
for i in range(len(areas)):
    ans += areas[i] * sides[i]

print(ans)       