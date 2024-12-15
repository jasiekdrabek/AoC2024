def parse_grid(grid):
    robot = None
    boxes = set()
    walls = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                robot = (x, y)
            elif cell == 'O':
                boxes.add((x, y))
            elif cell == '#':
                walls.add((x, y))

    return robot, boxes, walls

def move_robot_and_boxes(robot, boxes, walls, moves):
    # Direction vectors for movements
    directions = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }

    for move in moves:
        dx, dy = directions[move]
        new_robot = (robot[0] + dx, robot[1] + dy)

        # Check if the robot moves into a box
        if new_robot in boxes:
            box = new_robot
            new_box = (box[0] + dx, box[1] + dy)

            # Determine if any box in the chain would hit a wall
            chain = [box]
            while chain[-1] in boxes:
                next_box = (chain[-1][0] + dx, chain[-1][1] + dy)
                chain.append(next_box)

            # If the last box in the chain would hit a wall, cancel the move
            if chain[-1] in walls:
                continue
            chain = chain[1:]
            # Move all boxes in the chain
            for b in reversed(chain):
                boxes.add(b)
                next_box = (b[0] - dx, b[1] - dy)
                boxes.remove(next_box)

        # Update robot position if not moving into a wall
        if new_robot not in walls and new_robot not in boxes:
            robot = new_robot

    return robot, boxes

def format_grid(robot, boxes, walls, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]

    for x, y in walls:
        grid[y][x] = '#'

    for x, y in boxes:
        grid[y][x] = 'O'

    rx, ry = robot
    grid[ry][rx] = '@'

    return '\n'.join(''.join(row) for row in grid)

# Read input grid and moves from file
with open('15.txt', 'r') as f:
    lines = f.readlines()

# Separate grid and moves
input_grid = [line.strip() for line in lines if line.startswith('#') or line.startswith('.')]
input_moves = ''.join(line.strip() for line in lines if not line.startswith('#') and not line.startswith('.'))

# Parse the initial state
robot, boxes, walls = parse_grid(input_grid)

# Simulate the movements
robot, boxes = move_robot_and_boxes(robot, boxes, walls, input_moves)

# Output the final state
final_grid = format_grid(robot, boxes, walls, len(input_grid[0]), len(input_grid))
print(final_grid)

# Calculate the sum of all box coordinates
box_sum = sum(x + 100 * y for x, y in boxes)
print(f"Sum of all box coordinates (100*x + y): {box_sum}")