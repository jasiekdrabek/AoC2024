import re
import sys
from typing import Iterator

WIDTH = 101
HEIGHT = 103


def parse_input(lines: Iterator[str]) -> Iterator[tuple[int, int, int, int]]:
    for line in lines:
        yield tuple(map(int, re.findall(r'-?\d+', line)))


def simulate_robot(robot: tuple[int, int, int, int], steps: int) -> tuple[int, int]:
    px, py, vx, vy = robot
    return (px + vx * steps) % WIDTH, (py + vy * steps) % HEIGHT

def find_easter_egg(robots: list[tuple[int, int, int, int]]) -> int:
    lines = [set((x, y) for x in range(WIDTH)) for y in range(HEIGHT)]
    for i in range(WIDTH * HEIGHT):
        robot_positions = set(simulate_robot(robot, i) for robot in robots)
        max_line, y = max((len(robot_positions & line), y) for y, line in enumerate(lines))
        if max_line >= 30:
            contiguous = 0
            for x in range(WIDTH):
                if (x, y) in robot_positions:
                    contiguous += 1
                else:
                    contiguous = 0
                if contiguous == 30:
                    return i


def main():
    with open('14.txt', 'r') as file:
        robots = list(parse_input(file))
        print(find_easter_egg(robots))


if __name__ == '__main__':
    main()