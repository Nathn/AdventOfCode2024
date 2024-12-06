map_, infinite_position_count, n_test = [], 0, 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data, i = f.readlines(), 0
    for i, line in enumerate(data):
        map_.append([j for j in line.strip()])
    len_x = len(map_[0])
    len_y = len(map_)
def move(temp_map, position_history_map, i, j, direction):
    directions = { "^": (-1, 0, ">"), "v": (1, 0, "<"), "<": (0, -1, "^"), ">": (0, 1, "v") }
    di, dj, next_direction = directions[direction]
    while 0 <= i + di < len_y and 0 <= j + dj < len_x and temp_map[i + di][j + dj] == ".":
        if position_history_map is not None: position_history_map[i][j] = "X"
        temp_map[i + di][j + dj] = direction
        temp_map[i][j] = "."
        i += di; j += dj
    if 0 <= i + di < len_y and 0 <= j + dj < len_x and temp_map[i + di][j + dj] == "#":
        temp_map[i][j] = next_direction
    elif not (0 <= i + di < len_y and 0 <= j + dj < len_x): # Out of bounds
        if position_history_map is not None: position_history_map[i][j] = "X"
        temp_map[i][j] = "."
temp_map = [[cell for cell in row] for row in map_]
position_history_map = [[cell for cell in row] for row in map_]
guard_position = lambda _map_: next(((i, j, cell) for i, row in enumerate(_map_) for j, cell in enumerate(row) if cell in ["^", "v", "<", ">"]), (-1, -1, None))
while True: # Initial problem without new obstacles, to know which cells are never visited
    i, j, direction = guard_position(temp_map)
    if i == -1: break
    move(temp_map, position_history_map, i, j, direction)
total_test = len([cell for row in map_ for cell in row if cell == "."])
for i, row in enumerate(map_):
    for j, cell in enumerate(row):
        if cell != ".": continue # Can't place a obstacle on a cell not empty
        temp_map = [[cell_ for cell_ in row_] for row_ in map_]
        temp_map[i][j] = "#"
        n_test += 1
        print(f"Test {n_test}/{total_test}")
        if position_history_map[i][j] != "X": continue # Cell never visited = obstacle useless on it
        position_history = []
        while True:
            x, y, direction = guard_position(temp_map)
            if x == -1: break
            move(temp_map, None, x, y, direction)
            if temp_map in position_history:
                infinite_position_count += 1
                break
            position_history.append([[cell_ for cell_ in row_] for row_ in temp_map])
print(infinite_position_count)
