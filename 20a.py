import networkx as nx
from itertools import combinations
G = nx.DiGraph()
ans = 0
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
print(len(path))            
for i,(x,y) in enumerate(path):
    possible_cheat = set()
    for x2,y2 in combinations(range(3),2):
        if x2+y2 == 2:
            possible_cheat.add((x+x2,y+y2))
            possible_cheat.add((x-x2,y+y2))
            possible_cheat.add((x+x2,y-y2))
            possible_cheat.add((x-x2,y-y2))
            possible_cheat.add((x+y2,y+x2))
            possible_cheat.add((x-y2,y+x2))
            possible_cheat.add((x+y2,y-x2))
            possible_cheat.add((x-y2,y-x2))
    for cheat in possible_cheat:
        if cheat in G.nodes:
            new_path = path.index(cheat)
            if new_path - i > 100:
                ans +=1
print(ans)