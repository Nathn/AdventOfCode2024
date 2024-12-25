with open('input.txt', 'r', encoding="utf-8") as f:
    locks, locks_num, keys, keys_num, temp, total = [], [], [], [], [], 0
    for line in f.readlines():
        if line == "\n":
            if temp[0][0] == "#":
                locks.append(temp)
            else:
                keys.append(temp)
            temp = []
        else:
            temp.append(line.strip())
    if temp and temp[0][0] == "#":
        locks.append(temp)
    elif temp:
        keys.append(temp)

for lock in locks:
    locks_num.append([0] * len(lock[0]))
    for i in range(len(lock[0])):
        j = 0
        while lock[j][i] == "#":
            j += 1
        locks_num[-1][i] = j - 1
for key in keys:
    keys_num.append([0] * len(key[0]))
    for i in range(len(key[0])):
        j = 0
        while key[j][i] == ".":
            j += 1
        keys_num[-1][i] = len(key) - (j + 1)

for lock in locks_num:
    for key in keys_num:
        ok = True
        for i in range(len(key)):
            if (lock[i] + key[i]) > len(lock):
                ok = False
                break
        total += ok

print(total)
