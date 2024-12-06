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
    print(x,y)
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
print(result)
print(len(result))
