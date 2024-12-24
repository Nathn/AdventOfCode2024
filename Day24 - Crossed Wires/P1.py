with open('input.txt', 'r', encoding="utf-8") as f:
    variables, assignements, spart = {}, [], False
    for line in f.readlines():
        if line == "\n":
            spart = True
        elif not spart:
            line = line.strip().split(": ")
            variables[line[0]] = int(line[1])
        else:
            line = line.strip().split(" -> ")
            assignements.append((line[1], line[0].split(" ")))

i = 0
while assignements:
    if assignements[i][1][0] not in variables or assignements[i][1][2] not in variables:
        assignements.append(assignements.pop(i))
    else:
        var1, var2 = variables[assignements[i][1][0]], variables[assignements[i][1][2]]
        if assignements[i][1][1] == "AND":
            variables[assignements[i][0]] = var1 & var2
        elif assignements[i][1][1] == "OR":
            variables[assignements[i][0]] = var1 | var2
        elif assignements[i][1][1] == "XOR":
            variables[assignements[i][0]] = var1 ^ var2
        assignements.pop(i)

variables = {key: value for key, value in variables.items() if key.startswith("z")}
variables = {key: value for key, value in sorted(variables.items(), key=lambda item: int(item[0][1:]), reverse=True)}

binary = "".join([str(variables[key]) for key in variables])

print(int(binary, 2))
