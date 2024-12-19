with open('input.txt', 'r', encoding="utf-8") as f:
    patterns, designs, total = [], [], 0
    for line in f.readlines():
        if len(patterns) > 0 and line != '\n':
            designs.append(line.strip())
        elif line != '\n':
            patterns= [pattern.strip() for pattern in line.split(',')]

def add_pattern(current, design_):
    if current == design_: return True
    if len(current) >= len(design_): return False
    missing_part = design_[len(current):]
    for pattern in patterns:
        if (len(missing_part) >= len(pattern) and
            missing_part[:len(pattern)] == pattern and
            add_pattern(current + pattern, design_)): return True
    return False

for design in designs:
    total += add_pattern("", design)
print(total)
