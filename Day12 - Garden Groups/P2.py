with open('input.txt', 'r', encoding="utf-8") as f:
    start, total, count = (0, 0), 0, 0
    grid = [list(line.strip()) for line in f.readlines()]
    x, y = len(grid), len(grid[0])
    plots, temp = {}, [[-1 for _ in range(y)] for _ in range(x)]

def fill(i, j, c):
    if i < 0 or i >= x or j < 0 or j >= y or temp[i][j] != -1 or grid[i][j] != grid[start[0]][start[1]]:
        return
    temp[i][j] = c
    if c not in plots:
        plots[c] = []
    plots[c].append((i, j))
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        fill(i + dx, j + dy, c)

for i in range(x):
    for j in range(y):
        if temp[i][j] == -1:
            start = (i, j)
            fill(i, j, count)
            count += 1

for c, _ in plots.items():
    area, sides = len(plots[c]), []
    for i, j in plots[c]:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + dx, j + dy
            if ni < 0 or ni >= x or nj < 0 or nj >= y or temp[ni][nj] != c:
                sides.append([(i, j, dx, dy)])
    while True: # Merge sides if they are adjacent. Can require multiple iterations, hence the while loop.
        changed = False
        i = 0
        while i < len(sides):
            j = i + 1
            while j < len(sides):
                if any(abs(s1[0] - s2[0]) == 1 - abs(s1[2])
                        and abs(s1[1] - s2[1]) == 1 - abs(s1[3])
                        and s1[2] == s2[2]
                        and s1[3] == s2[3] for s1 in sides[i] for s2 in sides[j]):
                    sides[i] += sides[j]
                    sides.pop(j)
                    changed = True
                else:
                    j += 1
            i += 1
        if not changed: break
    total += area * len(sides)
print(total)
