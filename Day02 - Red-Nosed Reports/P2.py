safes = 0
levels = []
with open('mininput.txt', 'r', encoding="utf-8") as f:
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
            break
        if level[i] > level[i + 1]:
            desc = True
        elif desc:
            safe = False
            break
        if level[i] < level[i + 1]:
            asc = True
        elif asc:
            safe = False
            break
        if level[i] > level[i + 1] + 3:
            safe = False
            break
        if level[i] < level[i + 1] - 3:
            safe = False
            break
    if safe:
        safes += 1
        print(level)
        print("Safe without a change")
        continue
    for i in range(len(level)):
        temp = level.copy()
        temp.pop(i)
        print("changing ", level, " to ", temp)
        safe = True
        desc = False
        asc = False
        for i in range(len(temp) - 1):
            if temp[i] == temp[i + 1]:
                safe = False
            if temp[i] > temp[i + 1]:
                desc = True
            elif desc:
                safe = False
            if temp[i] < temp[i + 1]:
                asc = True
            elif asc:
                safe = False
            if temp[i] > temp[i + 1] + 3:
                safe = False
            if temp[i] < temp[i + 1] - 3:
                safe = False
        if safe:
            safes += 1
            print(level)
            print("Safe with a change -> ", temp)
            break
    if not safe:
        print(level)
        print("Not safe")
print(safes)
