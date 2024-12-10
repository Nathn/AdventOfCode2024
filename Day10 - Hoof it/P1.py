with open('input.txt', 'r', encoding="utf-8") as f:
    data, trailheads, reached_nines, total = f.readlines(), [], [], 0
    tmap = [list(x.strip()) for x in data]

for i, l in enumerate(tmap):
    for j, c in enumerate(l):
        if tmap[i][j] == '0':
            trailheads.append((i, j))

def take_this_path(index, current_pos):
    if index == 9 and current_pos not in reached_nines:
        reached_nines.append(current_pos)
        return 1
    t1, t2, t3, t4 = 0, 0, 0, 0
    if current_pos[0] + 1 < len(tmap) and tmap[current_pos[0] + 1][current_pos[1]] == str(index + 1):
        t1 = take_this_path(
            index + 1, (current_pos[0] + 1, current_pos[1])) # Going down
    if current_pos[0] - 1 >= 0 and tmap[current_pos[0] - 1][current_pos[1]] == str(index + 1):
        t2 = take_this_path(
            index + 1, (current_pos[0] - 1, current_pos[1])) # Going up
    if current_pos[1] + 1 < len(tmap[0]) and tmap[current_pos[0]][current_pos[1] + 1] == str(index + 1):
        t3 = take_this_path(
            index + 1, (current_pos[0], current_pos[1] + 1)) # Going right
    if current_pos[1] - 1 >= 0 and tmap[current_pos[0]][current_pos[1] - 1] == str(index + 1):
        t4 = take_this_path(
            index + 1, (current_pos[0], current_pos[1] - 1)) # Going left
    return t1 + t2 + t3 + t4

for trailhead in trailheads:
    reached_nines = []
    total += take_this_path(0, trailhead)
print(total)
