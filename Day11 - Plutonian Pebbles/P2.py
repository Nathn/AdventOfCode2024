memory = {}
with open('input.txt', 'r', encoding="utf-8") as f:
    stones = list(map(int, ''.join(f.readlines()).strip().split()))

def calc_stone(stone, times):
    if (stone, times) in memory: return memory[(stone, times)]
    n_stone = [stone * 2024]
    if stone == 0: n_stone = [1]
    elif len(str(stone)) % 2 == 0:
        n_stone = [int(str(stone)[:len(str(stone)) // 2]), int(str(stone)[len(str(stone)) // 2:])]
    sum_ = len(n_stone) if times == 1 else sum(calc_stone(st, times - 1) for st in n_stone)
    memory[(stone, times)] = sum_
    return sum_

print(sum(calc_stone(stone, 75) for stone in stones))
