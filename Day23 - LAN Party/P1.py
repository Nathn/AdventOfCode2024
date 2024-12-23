with open('input.txt', 'r', encoding="utf-8") as f:
    connections, sets, trisets = [], {}, []
    for line in f.readlines():
        connections.append(line.strip().split("-"))

for connection in connections:
    sets.setdefault(connection[0], []).append(connection[1])
    sets.setdefault(connection[1], []).append(connection[0])

for key, value in sets.items():
    for val in value:
        for val_2 in value:
            if val != val_2 and val_2 in sets[val] and {key, val, val_2} not in trisets:
                trisets.append({key, val, val_2})

trisets = [triset for triset in trisets if any([True for value in triset if value.startswith("t")])]
print(len(trisets))
