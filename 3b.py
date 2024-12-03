import re
ans = 0
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
control_pattern = r"do\(\)|don't\(\)"
active = True
with open('3.txt', 'r') as file:
    for line in file:
        matches = re.finditer(rf"{control_pattern}|{mul_pattern}", line)
        for match in matches:
            if match.group(0) == "do()":
                active = True
            elif match.group(0) == "don't()":
                active = False
            else:
                if active:
                    x, y = map(int, match.groups())
                    ans += x*y
print(ans)