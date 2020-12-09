import sys

rules = []
visited = set()
acc = 0
index = 0

for value in sys.stdin.read().split("\n"):
    ins, val = value.split(' ')
    rules.append((ins, int(val)))

while index not in visited:
    visited.add(index)

    ins, val = rules[index]

    if ins == 'jmp':
        index += val
        continue

    if ins == 'acc':
        acc += val

    index += 1


print(acc)
