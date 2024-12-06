with open('input.txt', 'r', encoding="utf-8") as f:
    data, i, map_ = f.readlines(), 0, []
    for i, line in enumerate(data):
        map_.append([j for j in line.strip()])
    position_history_map = [[cell for cell in row] for row in map_]

def guard_position(_map_):
    for i, row in enumerate(_map_):
        for j, cell in enumerate(row):
            if cell in ["^", "v", "<", ">"]:
                return i, j, cell
    return -1, -1, None

def move(map_, position_history_map, i, j, direction):
    directions = { "^": (-1, 0, ">"), "v": (1, 0, "<"), "<": (0, -1, "^"), ">": (0, 1, "v") }
    di, dj, next_direction = directions[direction]
    while 0 <= i + di < len(map_) and 0 <= j + dj < len(map_[0]) and map_[i + di][j + dj] == ".":
        map_[i + di][j + dj] = direction
        map_[i][j], position_history_map[i][j] = ".", "X"
        i += di; j += dj
    if 0 <= i + di < len(map_) and 0 <= j + dj < len(map_[0]) and map_[i + di][j + dj] == "#":
        map_[i][j] = next_direction
    elif not (0 <= i + di < len(map_) and 0 <= j + dj < len(map_[0])):
        map_[i][j], position_history_map[i][j] = ".", "X"
while True:
    i, j, direction = guard_position(map_)
    if i == -1: break
    move(map_, position_history_map, i, j, direction)
print("".join(["".join(row) for row in position_history_map]).count("X"))
