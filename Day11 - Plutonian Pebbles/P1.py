with open('input.txt', 'r', encoding="utf-8") as f:
    stones = [stone.strip() for stone in ''.join(f.readlines()).strip().split(' ')]

for i in range(25):
    print(f"{i}/{25}")
    n_stones = []
    for j, stone in enumerate(stones):
        if stone == '0':
            n_stones.append('1')
        elif len(stone) % 2 == 0:
            n_stones.append(stone[:len(stone) // 2].lstrip("0") or "0")
            n_stones.append(stone[len(stone) // 2:].lstrip("0") or "0")
        else:
            n_stones.append(str(int(stone) * 2024))
    stones = n_stones

print(len(stones))
