import re

result = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    for o in re.findall(r"mul\((\d+),(\d+)\)", ''.join(f.readlines()).strip()):
        result += int(o[0]) * int(o[1])
print(result)
