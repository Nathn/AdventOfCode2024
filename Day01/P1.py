list1, list2, diff = [], [], 0
with open('./Day01/input.txt', 'r', encoding="utf-8") as f:
    data = f.readlines()
    for line in enumerate(data):
        list1.append(int(line[1].split()[0]))
        list2.append(int(line[1].split()[1]))
for i in range(len(list1)):
    min1 = min(list1)
    list1.remove(min1)
    min2 = min(list2)
    list2.remove(min2)
    diff += abs(min1 - min2)
print(diff)
