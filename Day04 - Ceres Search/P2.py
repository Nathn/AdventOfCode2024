def check_diagonal_patterns(d, x, y):
    ptrns = [(a, b, c, d) for a, b in [('S', 'M'), ('M', 'S')] for c, d in [('M', 'S'), ('S', 'M')]]
    if (x + 1 < len(d) and x - 1 >= 0 and y + 1 < len(d[0]) and y - 1 >= 0):
        for pattern in ptrns:
            if (d[x + 1][y + 1] == pattern[0] and d[x - 1][y - 1] == pattern[1] and
                d[x + 1][y - 1] == pattern[2] and d[x - 1][y + 1] == pattern[3]):
                return True
    return False
count = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data = [x.strip() for x in f.readlines()]
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            count += char == 'A' and check_diagonal_patterns(data, i, j)
print(count)
