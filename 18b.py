import networkx as nx
rows = 71#7
cols = 71#7
b = 1024#12
start = (0,0)
end = (rows-1,cols-1)
G = nx.DiGraph()
obs = []
grid =[['.' for i in range(rows)] for j in range(cols)]
with open("18.txt") as file:
    for i,line in enumerate(file):
        line = line.strip()
        x,y = line.split(',')
        x,y = int(x),int(y)
        if i <= 1024:
            grid[x][y] = '#'
        else:
            obs.append((x,y))
        
for x in range(rows):
    for y in range(cols):
        if grid[x][y] == '.':
            G.add_node((x,y))
            
for x in range(rows):
    for y in range(cols):
        if x < rows-1:
            if grid[x + 1][y] == '.':
                G.add_edge((x,y),(x+1,y))
        if y < cols-1:
            if grid[x][y+1] == '.':
                G.add_edge((x,y),(x,y+1))
        if x > 0:
            if grid[x - 1][y] == '.':
                G.add_edge((x,y),(x-1,y))
        if y > 0:
            if grid[x][y-1] == '.':
                G.add_edge((x,y),(x,y-1))
while True :
    try:
        (x,y) = obs[0]
        obs = obs[1:]
        grid[x][y] = '#'
        G.remove_node((x,y))
        nx.shortest_path_length(G=G,source=start,target=end)
    except:
        break
    
print(x,y)
    