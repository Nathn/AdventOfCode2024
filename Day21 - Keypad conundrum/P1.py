with open('input.txt', 'r', encoding="utf-8") as f:
    codes, total = [], 0
    for line in f.readlines():
        codes.append(line.strip())

numeric_keypad = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

directional_keypad = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

def find_char(char, keypad=numeric_keypad):
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == char:
                return (i, j)

robot_num = (3, 2) # On numeric keypad
robots_dir = [(0, 2) for _ in range(2)] # On directional keypad

def go_to(c, times, robots):
    combination_temp = ""
    while directional_keypad[robots[0][0]][robots[0][1]] != c:
        c_pos = find_char(c, keypad=directional_keypad)
        if c_pos[0] > robots[0][0]:
            if len(robots) == 1:
                combination_temp += 'v' * (c_pos[0] - robots[0][0])
            else:
                gt, robots[1:] = go_to('v', c_pos[0] - robots[0][0], robots[1:])
                combination_temp += gt
            robots[0] = (c_pos[0], robots[0][1])
        if (c_pos[1] < robots[0][1] and
            directional_keypad[robots[0][0]][robots[0][1] - (robots[0][1] - c_pos[1])] != ' '):
            if len(robots) == 1:
                combination_temp += '<' * (robots[0][1] - c_pos[1])
            else:
                gt, robots[1:] = go_to('<', robots[0][1] - c_pos[1], robots[1:])
                combination_temp += gt
            robots[0] = (robots[0][0], c_pos[1])
        if c_pos[1] > robots[0][1]:
            if len(robots) == 1:
                combination_temp += '>' * (c_pos[1] - robots[0][1])
            else:
                gt, robots[1:] = go_to('>', c_pos[1] - robots[0][1], robots[1:])
                combination_temp += gt
            robots[0] = (robots[0][0], c_pos[1])
        if (c_pos[0] < robots[0][0] and
            directional_keypad[robots[0][0] - (robots[0][0] - c_pos[0])][robots[0][1]] != ' '):
            if len(robots) == 1:
                combination_temp += '^' * (robots[0][0] - c_pos[0])
            else:
                gt, robots[1:] = go_to('^', robots[0][0] - c_pos[0], robots[1:])
                combination_temp += gt
            robots[0] = (c_pos[0], robots[0][1])
    if len(robots) == 1:
        combination_temp += 'A' * times
    else:
        gt, robots[1:] = go_to('A', times, robots[1:])
        combination_temp += gt
    return combination_temp, robots

for code in codes:
    combination = ''
    for char in code:
        while numeric_keypad[robot_num[0]][robot_num[1]] != char:
            char_pos = find_char(char)
            if char_pos[0] > robot_num[0] and numeric_keypad[char_pos[0]][robot_num[1]] != ' ':
                gt, robots_dir = go_to('v', char_pos[0] - robot_num[0], robots_dir)
                combination += gt
                robot_num = (char_pos[0], robot_num[1])
            if char_pos[1] < robot_num[1] and numeric_keypad[robot_num[0]][char_pos[1]] != ' ':
                gt, robots_dir = go_to('<', robot_num[1] - char_pos[1], robots_dir)
                combination += gt
                robot_num = (robot_num[0], char_pos[1])
            if char_pos[1] > robot_num[1]:
                gt, robots_dir = go_to('>', char_pos[1] - robot_num[1], robots_dir)
                combination += gt
                robot_num = (robot_num[0], char_pos[1])
            if char_pos[0] < robot_num[0]:
                gt, robots_dir = go_to('^', robot_num[0] - char_pos[0], robots_dir)
                combination += gt
                robot_num = (char_pos[0], robot_num[1])
        gt, robots_dir = go_to('A', 1, robots_dir)
        combination += gt
    total += len(combination) * int("".join([c for c in code if c.isdigit()]))
print(total)
