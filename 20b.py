import networkx as nx
from itertools import combinations
G = nx.DiGraph()
ans,ans2 = 0,0
grid =[]
with open("20.txt") as file:
    for line in file:
        line = line.strip()
        grid.append(list(line))
rows = len(grid)
cols = len(grid[0])
start = (1,1)
end = (rows-1,cols-1)
for x in range(rows):
    for y in range(cols):
        if grid[x][y] == 'E':
            end = (x,y)
        if grid[x][y] == 'S':
            start = (x,y)
        if grid[x][y] != '#':
            G.add_node((x,y))

  
for (x,y) in G.nodes:
    if (x+1,y) in G.nodes:
        G.add_edge((x,y),(x+1,y))
    if (x,y+1) in G.nodes:
        G.add_edge((x,y),(x,y+1))
    if (x-1,y) in G.nodes:
        G.add_edge((x,y),(x-1,y)) 
    if (x,y-1) in G.nodes:
        G.add_edge((x,y),(x,y-1))           
path = nx.shortest_path(G,start,end)
dist = {}
d = 0
for p in path:
    dist[p] = d
    d += 1     
for (x,y),(x2,y2) in combinations(dist.items(),2):
    d = abs(x[0] -x2[0]) + abs(x[1] - x2[1])
    if d == 2 and y2 - y  - d >= 100:
        ans +=1
    if 2<= d <= 20 and y2 - y  - d>= 100:
        ans2 +=1
    
print(ans,ans2)