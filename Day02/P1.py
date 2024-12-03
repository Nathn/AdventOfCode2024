safes = 0
levels = []
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for line in data:
        levels.append(line.strip().split())
        levels = [[int(j) for j in i] for i in levels]
for level in levels:
    safe = True
    desc = False
    asc = False
    for i in range(len(level) - 1):
        if level[i] == level[i + 1]:
            safe = False
            print(level)
            print("equal")
            break
        if level[i] > level[i + 1]:
            desc = True
        elif desc:
            print(level)
            print("desc but should not")
            safe = False
            break
        if level[i] < level[i + 1]:
            asc = True
        elif asc:
            print(level)
            print("asc but should not")
            safe = False
            break
        if level[i] > level[i + 1] + 3:
            safe = False
            print(level)
            print("decrease by more than 3")
            break
        if level[i] < level[i + 1] - 3:
            safe = False
            print(level)
            print("increase by more than 3")
            break
    if safe:
        print(level)
        print("safe")
        safes += 1
print(safes)
