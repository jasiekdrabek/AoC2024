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
            target_values = [int(x.split("=")[1]) + 10000000000000, int(y.split("=")[1]) + 10000000000000]
        elif line == "":
            det = A_values[0] * B_values[1] - A_values[1] * B_values[0]
            if det != 0:
                x = (target_values[0] * B_values[1] - target_values[1] * B_values[0]) / det
                y = (A_values[0] * target_values[1] - A_values[1] * target_values[0]) / det

                if x.is_integer() and y.is_integer():
                    x, y = int(x), int(y)
                    cost = 3 * x + 1 * y
                    ans += cost
                    print(f"A: {A_values}, B: {B_values}, target: {target_values}, Solution: ({x}, {y}), Cost: {cost}")
                else:
                    print(f"A: {A_values}, B: {B_values}, target: {target_values}, Solution not integers")
            else:
                print(f"A: {A_values}, B: {B_values}, target: {target_values}, No solution (determinant = 0)")

            A_values = []
            B_values = []
            target_values = []


print(ans)