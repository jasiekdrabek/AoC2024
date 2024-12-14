def parse_input(data):
    """Parses the input data and returns a list of robots with positions and velocities."""
    robots = []
    for line in data:
        parts = line.split()
        position = tuple(map(int, parts[0][2:].split(",")))
        velocity = tuple(map(int, parts[1][2:].split(",")))
        robots.append({"position": position, "velocity": velocity})
    return robots

def move_robots(robots, grid_x, grid_y, steps):
    """Simulates robot movements over a given number of steps."""
    for robot in robots:
        x, y = robot["position"]
        vx, vy = robot["velocity"]
        new_x = (x + vx * steps) % (grid_x + 1)
        new_y = (y + vy * steps) % (grid_y + 1)
        robot["position"] = (new_x, new_y)

    return robots

def format_output(robots):
    """Formats the output positions of robots."""
    return [robot["position"] for robot in robots]

with open('14.txt', 'r') as file:
    grid_x, grid_y = 100, 102
    steps = 100
    robots = parse_input(file)
    final_positions = move_robots(robots, grid_x, grid_y, steps)
    quadrants = [0,0,0,0]
    for i, (x,y) in enumerate(format_output(final_positions), 1):
        if 0<=x<=grid_x/2 - 1 and 0<=y<=grid_y/2 - 1:
            quadrants[0] +=1
        if grid_x/2+1<=x<=grid_x and 0<=y<=grid_y/2 - 1:
            quadrants[1] +=1
        if 0<=x<=grid_x/2 - 1 and grid_y/2+1<=y<=grid_y:
            quadrants[2] +=1
        if grid_x/2+1<=x<=grid_x and grid_y/2+1<=y<=grid_y:
            quadrants[3] +=1
    ans = 1
    for quadrant in quadrants:
        ans *= quadrant
    print(ans)
