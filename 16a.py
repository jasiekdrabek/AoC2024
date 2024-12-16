from heapq import heappush, heappop

def parse_maze(file_path):
    """Parses the maze from the file and finds start (S) and end (E) points."""
    maze = []
    start, end = None, None

    with open(file_path, 'r') as f:
        for y, line in enumerate(f):
            row = line.strip()
            maze.append(row)
            if 'S' in row:
                start = (row.index('S'), y)
            if 'E' in row:
                end = (row.index('E'), y)

    return maze, start, end

def get_neighbors(position, direction):
    """Returns possible moves and their directions based on current direction."""
    x, y = position
    directions = {
        'right': ((1, 0), 'down', 'up'),
        'down': ((0, 1), 'left', 'right'),
        'left': ((-1, 0), 'up', 'down'),
        'up': ((0, -1), 'right', 'left')
    }

    forward_move = directions[direction][0]
    turn_left = directions[direction][1]
    turn_right = directions[direction][2]

    return {
        'forward': (x + forward_move[0], y + forward_move[1]),
        'left': turn_left,
        'right': turn_right
    }

def heuristic(pos, end):
    """Calculates the Manhattan distance heuristic."""
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

def find_path(maze, start, end):
    """Finds the shortest path from start to end using A* algorithm."""
    open_set = []
    heappush(open_set, (0, start, 'right', 0))  # (priority, position, direction, cost)
    visited = set()

    while open_set:
        _, current_pos, current_dir, current_cost = heappop(open_set)

        if current_pos == end:
            return current_cost

        if (current_pos, current_dir) in visited:
            continue

        visited.add((current_pos, current_dir))

        neighbors = get_neighbors(current_pos, current_dir)

        # Forward move
        forward_pos = neighbors['forward']
        if maze[forward_pos[1]][forward_pos[0]] != '#' and (forward_pos, current_dir) not in visited:
            heappush(open_set, (current_cost + 1 + heuristic(forward_pos, end), forward_pos, current_dir, current_cost + 1))

        # Turn left
        left_dir = neighbors['left']
        if (current_pos, left_dir) not in visited:
            heappush(open_set, (current_cost + 1000 + heuristic(current_pos, end), current_pos, left_dir, current_cost + 1000))

        # Turn right
        right_dir = neighbors['right']
        if (current_pos, right_dir) not in visited:
            heappush(open_set, (current_cost + 1000 + heuristic(current_pos, end), current_pos, right_dir, current_cost + 1000))

    return -1  # No path found

if __name__ == "__main__":
    maze, start, end = parse_maze('16.txt')
    cost = find_path(maze, start, end)
    print(f"The minimum cost to reach the end is: {cost}")
