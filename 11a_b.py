from  math import  floor, log10, pow
from functools import cache
stones = []
with open('11.txt', 'r') as file:
    for line in file:
        line = line.strip()
        stones =[int(l) for l in line.split(" ")]
@cache
def blink(stone,depth):
    if depth == 0:
        return 1
    if stone == 0:
        return blink(1,depth-1)
    elif (floor(log10(stone)) + 1) % 2 == 0:
        rule_2 = (floor(log10(stone)) + 1) /2
        right = int(stone // pow(10, rule_2))
        left = int(stone % pow(10, rule_2))
        return blink(right, depth -1) + blink(left,depth - 1)
    else:
        return blink(stone * 2024, depth - 1)
    
print(sum(blink(stone,25) for stone in stones))
print(sum(blink(stone,75) for stone in stones))

