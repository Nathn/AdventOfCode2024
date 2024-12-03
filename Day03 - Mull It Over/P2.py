import re

result = 0
on = True
with open('input.txt', 'r', encoding="utf-8") as f:
    data = ''.join(f.readlines()).strip()
occurences = re.findall(r"(?P<mul>mul\((\d+),(\d+)\))|(?P<dont>don\'t\(\))|(?P<do>do\(\))", data)
for o in occurences:
    if o[0] and on:
        result += int(o[1]) * int(o[2])
    elif o[3]:
        on = False
    elif o[4]:
        on = True
print(result)
