with open('input.txt', 'r', encoding="utf-8") as f:
    initial, total = [], 0
    for line in f.readlines():
        initial.append(int(line.strip()))

mix = lambda a, b: a ^ b
prune = lambda a: a % 16777216

for secret in initial:
    for _ in range(2000):
        secret = prune(mix(secret * 64, secret))
        secret = prune(mix(secret // 32, secret))
        secret = prune(mix(secret * 2048, secret))
    total += secret

print(total)
