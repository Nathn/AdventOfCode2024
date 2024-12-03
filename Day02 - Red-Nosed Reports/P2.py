def is_safe(level):
    desc, asc = False, False
    for i in range(len(level) - 1):
        if level[i] == level[i + 1] or abs(level[i] - level[i + 1]) > 3:
            return False
        if level[i] > level[i + 1]:
            if asc:
                return False
            desc = True
        elif level[i] < level[i + 1]:
            if desc:
                return False
            asc = True
    return True

safes = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    levels = [[int(i) for i in line.strip().split()] for line in data]

for level in levels:
    if is_safe(level):
        safes += 1
        continue
    for i in range(len(level)):
        temp = level.copy()
        temp.pop(i)
        if is_safe(temp):
            safes += 1
            break

print(safes)
