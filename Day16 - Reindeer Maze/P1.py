with open('input.txt', 'r', encoding="utf-8") as f:
    walls, start, end, v, x, y = set(), ((-1, -1), (0, 1)), (-1, -1), 0, 0, 0
    for line in f.readlines():
        x = 0
        for c in line.strip():
            if c == "#":
                walls.add((y, x))
            elif c == "S":
                start = ((y, x), (0, 1))
            elif c == "E":
                end = (y, x)
            x += 1
        y += 1
    max_y = y
    max_x = x

max_v = max_y * max_x - len(walls)

def find_moves(position):
    res = []
    y, x = position
    moves = [(y + dy, x + dx) for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
    for m in moves:
        if (m not in walls):
            res.append(m)
    return res

def count_score(dir, next_dir, total):
    if dir == next_dir:
        total += 1
        return total
    else:
        total += 1001
        return total

history = set()
shortest_path_tree = {}
shortest_path_tree[start[0]] = [start[0], start[1], 0]

while v < len(shortest_path_tree):
    v = 0
    for position in shortest_path_tree.copy():
        dir = shortest_path_tree[position][1]
        distance = shortest_path_tree[position][2]
        if position == end:
            v += 1
            continue
        v += position in history
        history.add(position)
        moves = find_moves(position)
        v += not moves
        for move in moves:
            t = count_score(dir, (move[0] - position[0], move[1] - position[1]), distance)
            if move in shortest_path_tree:
                if t < shortest_path_tree[move][2]:
                    shortest_path_tree[move][0] = position
                    shortest_path_tree[move][1] = (move[0] - position[0], move[1] - position[1])
                    shortest_path_tree[move][2] = t
            else:
                shortest_path_tree[move] = [position, (move[0] - position[0], move[1] - position[1]), t]

print(shortest_path_tree[end][2])
