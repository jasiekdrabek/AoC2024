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


def find_all_paths(maze, start, end):
    """Finds all shortest paths from start to end and calculates unique positions."""
    directions = ['right', 'down', 'left', 'up']
    open_set = []
    heappush(open_set, (0, start, 'right', 0, set([start])))  # (priority, position, direction, cost, path_set)
    visited = {}
    min_cost = float('inf')
    unique_positions = set()

    while open_set:
        _, current_pos, current_dir, current_cost, path_set = heappop(open_set)

        # Stop if we've exceeded the minimum cost found so far
        if current_cost > min_cost:
            continue

        # If we reach the end, update the minimum cost and add positions
        if current_pos == end:
            if current_cost < min_cost:
                min_cost = current_cost
                unique_positions = path_set
            elif current_cost == min_cost:
                unique_positions.update(path_set)
            continue

        # Avoid re-processing positions with higher or equal cost
        if (current_pos, current_dir) in visited and visited[(current_pos, current_dir)] < current_cost:
            continue

        visited[(current_pos, current_dir)] = current_cost

        neighbors = get_neighbors(current_pos, current_dir)

        # Forward move
        forward_pos = neighbors['forward']
        if maze[forward_pos[1]][forward_pos[0]] != '#':
            heappush(open_set, (
                current_cost + 1 + heuristic(forward_pos, end),
                forward_pos,
                current_dir,
                current_cost + 1,
                path_set | {forward_pos}
            ))

        # Turn left
        left_dir = neighbors['left']
        heappush(open_set, (
            current_cost + 1000 + heuristic(current_pos, end),
            current_pos,
            left_dir,
            current_cost + 1000,
            path_set
        ))

        # Turn right
        right_dir = neighbors['right']
        heappush(open_set, (
            current_cost + 1000 + heuristic(current_pos, end),
            current_pos,
            right_dir,
            current_cost + 1000,
            path_set
        ))

    return len(unique_positions)


if __name__ == "__main__":
    maze, start, end = parse_maze('16.txt')
    unique_positions = find_all_paths(maze, start, end)
    print(f"The number of unique positions in all shortest paths is: {unique_positions}")
