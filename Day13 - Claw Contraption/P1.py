import re

with open('input.txt', 'r', encoding="utf-8") as f:
    prizes, total = [], 0
    ba, bb, prize = (0, 0), (0, 0), (0, 0)
    for line in f.readlines():
        if line.startswith("Button A:"):
            ba = re.findall(r'\d+', line)
        elif line.startswith("Button B:"):
            bb = re.findall(r'\d+', line)
        elif line.startswith("Prize:"):
            prize = re.findall(r'\d+', line)
            prizes.append((int(prize[0]), int(prize[1]), int(ba[0]), int(ba[1]), int(bb[0]), int(bb[1])))

for prize in prizes:
    det = prize[2] * prize[5] - prize[4] * prize[3]
    if det == 0:
        continue # No unique solution exists
    delta_X = prize[0] * prize[5] - prize[4] * prize[1]
    delta_Y = prize[2] * prize[1] - prize[0] * prize[3]
    if delta_X % det != 0 or delta_Y % det != 0:
        continue # No integer solution exists
    total += (delta_X // det) * 3 + (delta_Y // det)

print(total)
