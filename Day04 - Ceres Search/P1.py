def check_pattern(d, x, y, dirx, diry):
    if (0 <= x < len(d) and 0 <= y < len(d[0]) and
        0 <= x + dirx < len(d) and 0 <= y + diry < len(d[0]) and
        0 <= x + 2 * dirx < len(d) and 0 <= y + 2 * diry < len(d[0]) and
        0 <= x + 3 * dirx < len(d) and 0 <= y + 3 * diry < len(d[0])):
        return (d[x][y] == 'X' and
                d[x + dirx][y + diry] == 'M' and
                d[x + 2 * dirx][y + 2 * diry] == 'A' and
                d[x + 3 * dirx][y + 3 * diry] == 'S')
    return False

count = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data = [x.strip() for x in f.readlines()]
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'X':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    count += not (dx == 0 and dy == 0) and check_pattern(data, i, j, dx, dy)
print(count)
