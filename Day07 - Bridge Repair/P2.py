
eqs, total = {}, 0
with open('input.txt', 'r', encoding="utf-8") as f:
    for line in f.readlines():
        eqs[line.strip().split(":")[0].strip()] = line.strip().split(":")[1].strip().split(" ")

def multiplication(numbers, current_total, current_subtotal, result):
    if len(numbers) == 0:
        if current_subtotal <= result:
            current_total.append(current_subtotal)
        return current_total
    current_subtotal = current_subtotal * numbers[0]
    if current_subtotal <= result:
        addition(numbers[1:], current_total, current_subtotal, result)
        multiplication(numbers[1:], current_total, current_subtotal, result)
        concatenation(numbers[1:], current_total, current_subtotal, result)
    return current_total

def addition(numbers, current_total, current_subtotal, result):
    if len(numbers) == 0:
        if current_subtotal <= result:
            current_total.append(current_subtotal)
        return current_total
    current_subtotal = current_subtotal + numbers[0]
    if current_subtotal <= result:
        addition(numbers[1:], current_total, current_subtotal, result)
        multiplication(numbers[1:], current_total, current_subtotal, result)
        concatenation(numbers[1:], current_total, current_subtotal, result)
    return current_total

def concatenation(numbers, current_total, current_subtotal, result):
    if len(numbers) == 0:
        if current_subtotal <= result:
            current_total.append(current_subtotal)
        return current_total
    current_subtotal = int(str(current_subtotal) + str(numbers[0]))
    if current_subtotal <= result:
        addition(numbers[1:], current_total, current_subtotal, result)
        multiplication(numbers[1:], current_total, current_subtotal, result)
        concatenation(numbers[1:], current_total, current_subtotal, result)
    return current_total

def is_valid(nbs, rt):
    current_total = []
    current_total = multiplication(nbs[1:], [], nbs[0], rt)
    current_total += addition(nbs[1:], [], nbs[0], rt)
    current_total += concatenation(nbs[1:], [], nbs[0], rt)
    return current_total

for res, nums in eqs.items():
    if int(res) in is_valid([int(num) for num in nums], int(res)):
        total += int(res)
print(total)

