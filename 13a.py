import numpy as np

A_values = []
B_values = []
target_values = []
ans = 0
with open('13.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith("Button A"):
            x, y = line.split(": ")[1].split(", ")
            A_values = [int(x.split("+")[1]), int(y.split("+")[1])]
        elif line.startswith("Button B"):
            x, y = line.split(": ")[1].split(", ")
            B_values = [int(x.split("+")[1]), int(y.split("+")[1])]
        elif line.startswith("Prize"):
            x, y = line.split(": ")[1].split(", ")
            target_values = [int(x.split("=")[1]), int(y.split("=")[1])]
        elif line == "":
            matrix = np.array([[A_values[0], B_values[0]], [A_values[1], B_values[1]]])
            target = np.array(target_values)
            determinant = np.linalg.det(matrix)
            if determinant != 0:
                solution = np.linalg.solve(matrix, target)
                x, y = np.round(solution).astype(int)
                if (x * A_values[0] + y * B_values[0] == target_values[0] and
                    x * A_values[1] + y * B_values[1] == target_values[1]):
                    cost = 3 * x + 1 * y
                    ans += cost
                    print(f"A: {A_values}, B: {B_values}, target: {target_values}, Solution: ({x}, {y}), Cost: {cost}")
                else:
                    print(f"A: {A_values}, B: {B_values}, target: {target_values}, Rounded solution does not satisfy equations")
            else:
                print(f"A: {A_values}, B: {B_values}, target: {target_values}, No solution (determinant = 0)")

            # Reset the values for the next block
            A_values = []
            B_values = []
            target_values = []

print(ans)