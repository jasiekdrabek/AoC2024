def find_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    reversed_word = word[::-1]
    directions = [
        (0, 1),  # Poziomo w prawo
        (1, 0),  # Pionowo w dół
        (1, 1),  # Diagonalnie w dół w prawo
        (1, -1), # Diagonalnie w dół w lewo
    ]

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def check_word(x, y, dx, dy):
        found_word = ""
        for i in range(len(word)):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny):
                return None
            found_word += grid[nx][ny]
        if found_word == word or found_word == reversed_word:
            return [(x + i * dx, y + i * dy) for i in range(len(word))]
        return None

    matches = []
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                match = check_word(i, j, dx, dy)
                if match:
                    matches.append(match)

    return matches

grid = []
with open('4.txt', 'r') as file:
    for line in file:
        grid.append(line[:-1])

result = find_xmas(grid)
print(len(result))

