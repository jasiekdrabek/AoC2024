def parse_grid(grid):
    robot = None
    left_box = set()
    right_box = set()
    walls = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '@':
                robot = (x, y)
            elif cell == '[':
                left_box.add((x, y))
            elif cell == ']':
                right_box.add((x, y))
            elif cell == '#':
                walls.add((x, y))

    return robot, left_box, right_box, walls

def move_robot_and_boxes(robot, left_box, right_box, walls, moves):
    # Direction vectors for movements
    directions = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-1, 0),
        '>': (1, 0)
    }
    
    directions_box = {
        '^': (0, -1),
        'v': (0, 1),
        '<': (-2, 0),
        '>': (2, 0)
    }
    def get_right_box(dx,dy,last):
        if (last[0] + dx, last[1] + dy) in walls:
            return
        elif (last[0] + dx, last[1] + dy) in right_box:
            right_chain.add((last[0] + dx, last[1] + dy))
            left_chain.add((last[0] + dx - 1,last[1] + dy))
            get_right_box(dx,dy,(last[0] + dx, last[1] + dy))
            get_left_box(dx,dy,(last[0] + dx - 1, last[1] + dy))
        elif (last[0] + dx, last[1] + dy) in left_box:
            right_chain.add((last[0] + dx + 1, last[1] + dy))
            left_chain.add((last[0] + dx, last[1] + dy))
            get_right_box(dx,dy,(last[0] + dx + 1, last[1] + dy))
            get_left_box(dx,dy,(last[0] + dx, last[1] + dy))
        
    def get_left_box(dx,dy,last):
        if (last[0] + dx, last[1] + dy) in walls:
            return
        elif (last[0] + dx, last[1] + dy) in left_box:
            left_chain.add((last[0] + dx, last[1] + dy))
            right_chain.add((last[0] + dx + 1,last[1] + dy))
            get_right_box(dx,dy,(last[0] + dx + 1, last[1] + dy))
            get_left_box(dx,dy,(last[0] + dx, last[1] + dy))
        elif (last[0] + dx, last[1] + dy) in right_box:
            right_chain.add((last[0] + dx, last[1] + dy))
            left_chain.add((last[0] + dx - 1, last[1] + dy))
            get_right_box(dx,dy,(last[0] + dx, last[1] + dy))
            get_left_box(dx,dy,(last[0] + dx - 1, last[1] + dy))

    for move in moves:
        dx, dy = directions[move]
        dx_box, dy_box = directions_box[move]
        new_robot = (robot[0] + dx, robot[1] + dy)
        left_chain = set()
        right_chain = set()
        can_move = True
        # Check if the robot moves into a box
        if new_robot in left_box or new_robot in right_box:
            box = new_robot
            if new_robot in left_box:
                left_chain.add(box)
                right_chain.add((box[0] + 1,box[1]))
                left_next_box = box
                right_next_box = (box[0] + 1,box[1])
            else:
                left_chain.add((box[0] - 1,box[1]))
                right_chain.add(box)
                left_next_box = (box[0] - 1,box[1])
                right_next_box = box
            # Get boxes to move
            while True:
                if move == '>' and left_next_box in left_box:
                    left_chain.add(left_next_box)
                    right_chain.add(right_next_box)
                elif move == '<' and right_next_box in right_box:
                    right_chain.add(right_next_box)
                    left_chain.add(left_next_box)
                else:
                    if move != '<' and move != '>':
                        get_left_box(dx,dy,left_next_box)
                        get_right_box(dx,dy,right_next_box)
                        break
                    else:
                        break
                left_next_box = (left_next_box[0] + dx_box, left_next_box[1] + dy_box)
                right_next_box = (right_next_box[0] + dx_box, right_next_box[1] + dy_box)

            # Determine if any box in the chain would hit a wall
            can_move = True
            for left in left_chain:
                if (left[0] + dx, left[1] + dy) in walls:
                    can_move = False
                    break
            for right in right_chain:
                if (right[0] + dx, right[1] + dy) in walls:
                    can_move = False
                    break
            if not can_move:
                continue
            
            # Move all boxes in the chain
            for b in left_chain:
                if b in left_box:
                    left_box.remove(b)
            for b in right_chain:
                if b in right_box:
                    right_box.remove(b)
            for b in left_chain:
                left_box.add((b[0] + dx, b[1] + dy))
            for b in right_chain:
                right_box.add((b[0] + dx, b[1] + dy))

        # Update robot position if not moving into a wall
        if new_robot not in walls and new_robot not in left_box and new_robot not in right_box:
            robot = new_robot

    return robot, left_box, right_box

def format_grid(robot, left_box, right_box, walls, width, height):
    grid = [['.' for _ in range(width)] for _ in range(height)]

    for x, y in walls:
        grid[y][x] = '#'
    for x, y in left_box:
        grid[y][x] = '['
    for x, y in right_box:
        grid[y][x] = ']'
    rx, ry = robot
    grid[ry][rx] = '@'

    return '\n'.join(''.join(row) for row in grid)

# Read input grid and moves from file
with open('15.txt', 'r') as f:
    lines = f.readlines()

# Separate grid and moves
input_grid = [line.strip().replace('#', '##').replace('O', '[]').replace('.','..').replace('@', '@.') for line in lines if line.startswith('#') or line.startswith('.')]
input_moves = ''.join(line.strip() for line in lines if not line.startswith('#') and not line.startswith('.'))

# Parse the initial state
robot, left_box, right_box, walls = parse_grid(input_grid)

# Simulate the movements
robot, left_box, right_box = move_robot_and_boxes(robot, left_box, right_box, walls, input_moves)

# Output the final state
#final_grid = format_grid(robot, left_box, right_box, walls, len(input_grid[0]), len(input_grid))
#print(final_grid)

# Calculate the sum of all box coordinates
box_sum = sum(x + 100 * y for x, y in left_box)
print(f"Sum of all box coordinates (100*x + y): {box_sum}")