def is_try_invalid(try_):
    for num in try_:
        related_rules = [rule for rule in rules if num == rule[0]]
        for rule in related_rules:
            try:
                if try_.index(rule[0]) >= try_.index(rule[1]):
                    return [True, rule]
            except ValueError:
                pass
    return [False, None]

rules, tries, total = [], [], 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data, i = f.readlines(), 0
    for i, line in enumerate(data):
        if not line.strip(): break
        rules.append([int(j) for j in line.strip().split("|")])
    for line in data[i + 1:]:
        tries.append([int(j) for j in line.strip().split(",")])
for try_ in [[try_, is_try_invalid(try_)[1]] for try_ in tries if is_try_invalid(try_)[0]]:
    is_try_still_invalid = [True, try_[1]]
    while is_try_still_invalid[0]:
        try_[0].insert(try_[0].index(try_[1][1]), try_[0].pop(try_[0].index(try_[1][0])))
        is_try_still_invalid = is_try_invalid(try_[0])
        try_[1] = is_try_still_invalid[1]
    total += try_[0][len(try_[0]) // 2]
print(total)
