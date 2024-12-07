eqs, total = {}, 0
with open('input.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        eqs[line.strip().split(":")[0].strip()] = line.strip().split(":")[1].strip().split(" ")

def is_valid(nbs, rt):
    if nbs[0] > rt or nbs[-1] > rt:
        return False
    if len(nbs) == 2:
        return rt in (nbs[0] + nbs[1], nbs[0] * nbs[1])
    return is_valid(nbs[:len(nbs) - 1], rt - nbs[-1]) or is_valid(nbs[:len(nbs) - 1], rt / nbs[-1])

for res, nums in eqs.items():
    if is_valid([int(num) for num in nums], int(res)):
        total += int(res)
print(total)
