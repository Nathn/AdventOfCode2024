list1, list2, sim_score = [], [], 0
with open('input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for line in enumerate(data):
        list1.append(int(line[1].split()[0]))
        list2.append(int(line[1].split()[1]))
for n in list1:
    count = list2.count(n)
    sim_score += n * count
print(sim_score)
