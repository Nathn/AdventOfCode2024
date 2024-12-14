import re

size_x, size_y = 101, 103
with open('input.txt', 'r', encoding="utf-8") as f:
    grid = [[[] for _ in range(size_x)] for _ in range(size_y)]
    for line in f.readlines():
        p = re.findall(r'-?\d+', line)
        grid[int(p[1])][int(p[0])].append((int(p[2]), int(p[3])))

for _ in range(100):
    new_grid = [[[] for _ in range(size_x)] for _ in range(size_y)]
    for y in range(size_y):
        for x in range(size_x):
            if len(grid[y][x]) == 0:
                continue
            for dx, dy in grid[y][x]:
                new_x = (x + dx) % size_x
                new_y = (y + dy) % size_y
                new_grid[new_y][new_x].append((dx, dy))
    grid = new_grid

middle_col = size_y // 2
middle_row = size_x // 2

grid_left_half = [[[item for item in grid[y][x]] for x in range(size_x // 2)] for y in range(size_y) if y != middle_col]
grid_right_half = [[[item for item in grid[y][x]] for x in range(size_x // 2, size_x)] for y in range(size_y) if y != middle_col]
grid_top_left = [[[item for item in grid[y][x]] for x in range(size_x // 2) if x != middle_row] for y in range(size_y // 2) if y != middle_col]
grid_top_right = [[[item for item in grid[y][x]] for x in range(size_x // 2, size_x) if x != middle_row] for y in range(size_y // 2) if y != middle_col]
grid_bottom_left = [[[item for item in grid[y][x]] for x in range(size_x // 2) if x != middle_row] for y in range(size_y // 2, size_y) if y != middle_col]
grid_bottom_right = [[[item for item in grid[y][x]] for x in range(size_x // 2, size_x) if x != middle_row] for y in range(size_y // 2, size_y) if y != middle_col]

def count_items(grid_):
    return sum([len(item) for row in grid_ for item in row])

print(count_items(grid_top_left) *
      count_items(grid_top_right) *
      count_items(grid_bottom_left) *
      count_items(grid_bottom_right))
