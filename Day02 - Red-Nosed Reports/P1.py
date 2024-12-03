safes = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    levels = [[int(i) for i in line.strip().split()] for line in data]

for level in levels:
    safe, desc, asc = True, False, False
    for i in range(len(level) - 1):
        if level[i] == level[i + 1] or abs(level[i] - level[i + 1]) > 3:
            safe = False
            break
        if level[i] > level[i + 1]:
            if asc:
                safe = False
                break
            desc = True
        elif level[i] < level[i + 1]:
            if desc:
                safe = False
                break
            asc = True
    safes += safe
print(safes)
