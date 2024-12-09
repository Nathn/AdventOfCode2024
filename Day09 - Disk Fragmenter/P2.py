with open('input.txt', 'r', encoding="utf-8") as f:
    data, count, filesystem = f.readlines(), 0, []
    old = data[0].strip()

for i, c in enumerate(old):
    if i % 2 == 0:
        filesystem += [(i // 2, int(c))]
    else:
        filesystem += [(None, int(c))]

j = len(filesystem) - 1
while j > 0:
    bindex = None
    if filesystem[j][0] is None:
        j -= 1
        continue
    for i, b in enumerate(filesystem):
        if i > j:
            break
        if b[0] is None and b[1] >= filesystem[j][1]:
            bindex = i
            break
    if i >= len(filesystem):
        j -= 1
        continue
    if bindex is not None:
        bi_content = filesystem[bindex]
        bj_content = filesystem[j]
        filesystem[bindex] = filesystem[j]
        filesystem[j] = (None, filesystem[j][1])
        if bi_content[1] > bj_content[1]:
            filesystem.insert(bindex + 1, (None, bi_content[1] - bj_content[1]))
    j -= 1

index = 0
for file in filesystem:
    for _ in range(file[1]):
        count += file[0] * index if file[0] is not None else 0
        index += 1
print(count)
