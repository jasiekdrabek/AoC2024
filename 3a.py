import re
ans = 0
with open('3.txt', 'r') as file:
    for line in file:
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, line)
        filtered_matches = [(int(x), int(y)) for x, y in matches if 1 <= int(x) <= 999 and 1 <= int(y) <= 999]
        ans += sum([x*y for x, y in filtered_matches])
print(ans)