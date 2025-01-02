with open('input.txt', 'r', encoding="utf-8") as f:
    map_, movements, total = [], [], 0
    for line in f.readlines():
        if line == '\n': movements = [1]
        elif len(movements) > 0 and line != '\n':
            if len(movements) == 1:
                movements = list(line.strip())
            else:
                movements += list(line.strip())
        elif line != '\n':
            map_.append(list(line.strip()))

def find_robot():
    for y, row_ in enumerate(map_):
        for x, cell_ in enumerate(row_):
            if cell_ == '@': return (x, y)

for movement in movements:
    robot = find_robot()
    if movement == '<':
        if map_[robot[1]][robot[0] - 1] == '#': continue
        if map_[robot[1]][robot[0] - 1] == 'O':
            box_x = robot[0] - 1
            while map_[robot[1]][box_x] == 'O':
                box_x -= 1
            if map_[robot[1]][box_x] == '#':
                continue
            box_x2 = robot[0] - 1
            while box_x < box_x2:
                map_[robot[1]][box_x2 - 1] = 'O'
                box_x2 -= 1
        map_[robot[1]][robot[0] - 1] = '@'
        map_[robot[1]][robot[0]] = '.'
    elif movement == '>':
        if map_[robot[1]][robot[0] + 1] == '#': continue
        if map_[robot[1]][robot[0] + 1] == 'O':
            box_x = robot[0] + 1
            while map_[robot[1]][box_x] == 'O':
                box_x += 1
            if map_[robot[1]][box_x] == '#':
                continue
            box_x2 = robot[0] + 1
            while box_x > box_x2:
                map_[robot[1]][box_x2 + 1] = 'O'
                box_x2 += 1
        map_[robot[1]][robot[0] + 1] = '@'
        map_[robot[1]][robot[0]] = '.'
    elif movement == '^':
        if map_[robot[1] - 1][robot[0]] == '#': continue
        if map_[robot[1] - 1][robot[0]] == 'O':
            box_y = robot[1] - 1
            while map_[box_y][robot[0]] == 'O':
                box_y -= 1
            if map_[box_y][robot[0]] == '#':
                continue
            box_y2 = robot[1] - 1
            while box_y < box_y2:
                map_[box_y2 - 1][robot[0]] = 'O'
                box_y2 -= 1
        map_[robot[1] - 1][robot[0]] = '@'
        map_[robot[1]][robot[0]] = '.'
    elif movement == 'v':
        if map_[robot[1] + 1][robot[0]] == '#': continue
        if map_[robot[1] + 1][robot[0]] == 'O':
            box_y = robot[1] + 1
            while map_[box_y][robot[0]] == 'O':
                box_y += 1
            if map_[box_y][robot[0]] == '#':
                continue
            box_y2 = robot[1] + 1
            while box_y > box_y2:
                map_[box_y2 + 1][robot[0]] = 'O'
                box_y2 += 1
        map_[robot[1] + 1][robot[0]] = '@'
        map_[robot[1]][robot[0]] = '.'

for i, row in enumerate(map_):
    for j, cell in enumerate(row):
        if cell == 'O':
            total += i * 100 + j
print(total)
