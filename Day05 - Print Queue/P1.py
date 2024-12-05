rules, tries, total = [], [], 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data, i = f.readlines(), 0
    for i, line in enumerate(data):
        if not line.strip(): break
        rules.append([int(j) for j in line.strip().split("|")])
    tries = [[int(j) for j in line.strip().split(",")] for line in data[i + 1:]]
for try_ in tries:
    invalid = False
    for i, num in enumerate(try_):
        for rule in [rule for rule in rules if num == rule[0]]:
            try:
                if try_.index(rule[0]) >= try_.index(rule[1]):
                    invalid = True
                    break
            except ValueError:
                pass
    if not invalid:
        total += try_[len(try_) // 2]
print(total)
