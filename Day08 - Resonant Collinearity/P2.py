with open('input.txt', 'r', encoding="utf-8") as f:
    data, count, o_map, n_map, antennas = f.readlines(), 0, [], [], {}
    for i, line in enumerate(data):
        o_map.append([j for j in line.strip()])
        n_map.append([j for j in line.strip()])

is_in_bounds = lambda i, j: 0 <= i < len(o_map) and 0 <= j < len(o_map[0])

for i, l in enumerate(o_map):
    for j, c in enumerate(l):
        if c != '.':
            if c not in antennas:
                antennas[c] = [(i, j)]
            else:
                antennas[c].append((i, j))

for k, v in antennas.items():
    if len(v) == 1:
        n_map[v[0][0]][v[0][1]] = '.'
        antennas.pop(k)
    for i, (a, b) in enumerate(v):
        for j, (x, y) in enumerate(v):
            if i < j:
                dx1, dx2 = a - abs(a - x), x + abs(x - a)
                dy1 = b + abs(b - y) if b > y else b - abs(b - y)
                dy2 = y - abs(b - y) if b > y else y + abs(y - b)
                while is_in_bounds(dx1, dy1):
                    n_map[dx1][dy1] = '#'
                    dx1 -= abs(a - x)
                    dy1 = dy1 + abs(b - y) if b > y else dy1 - abs(b - y)
                while is_in_bounds(dx2, dy2):
                    n_map[dx2][dy2] = '#'
                    dx2 += abs(x - a)
                    dy2 = dy2 - abs(b - y) if b > y else dy2 + abs(y - b)

for i, l in enumerate(n_map):
    for j, c in enumerate(l):
        count += c != '.'
print(count)
