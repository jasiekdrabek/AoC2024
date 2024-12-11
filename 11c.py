from  math import  floor, log10, pow
from collections import defaultdict
stones = []
with open('11.txt', 'r') as file:
    for line in file:
        line = line.strip()
        stones =[int(l) for l in line.split(" ")]

stones_dict = defaultdict(int)
for stone in stones:
    stones_dict[stone] = 1

def blink(depth):
    for _ in range(depth):
        stonework = dict(stones_dict)
        for key, value in stonework.items():
            if value == 0:
                continue
            if key == 0:
                stones_dict[1] += value
                stones_dict[key] -= value
            elif (floor(log10(key)) + 1) % 2 == 0:
                stone = key
                rule_2 = (floor(log10(stone)) + 1) /2
                right = int(stone // pow(10, rule_2))
                left = int(stone % pow(10, rule_2))
                stones_dict[right] += value 
                stones_dict[left] += value
                stones_dict[key] -= value
            else:
                stones_dict[key * 2024] += value
                stones_dict[key] -= value

blink(25)
print(sum(stones_dict.values()))
blink(50)
print(sum(stones_dict.values()))