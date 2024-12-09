with open('input.txt', 'r', encoding="utf-8") as f:
    data, count, filesystem = f.readlines(), 0, []
    old = data[0].strip()

for i, c in enumerate(old):
    if i % 2 == 0:
        filesystem += [str(i // 2) for _ in range(int(c))]
    else:
        filesystem += ['.' for _ in range(int(c))]

i = 0
j = len(filesystem) - 1
while j > i:
    if filesystem[j] == '.':
        j -= 1
        continue
    if filesystem[i] != '.':
        i += 1
        continue
    filesystem[i], filesystem[j] = filesystem[j], '.'
    i, j = i + 1, j - 1

for i, c in enumerate(filesystem):
    count += int(c) * i if c != '.' else 0
print(count)
