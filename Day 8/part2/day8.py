import sys


def calc(index, correct):
    visited = set()
    acc = 0
    # index = 0

    while index not in visited:
        if index >= len(rules):
            return None

        visited.add(index)

        ins, val = rules[index]

        if ins == 'acc':
            acc += val

        index += 1 if ins != 'jmp' else val
        if index == len(rules) - 1 or index in correct:
            return acc

    return None


rules = []
swapped = False
stack = []

for value in sys.stdin.read().split("\n"):
    ins, val = value.split(' ')
    rules.append((ins, int(val)))


#  Find out which instructions cause loops

# for instruction that dont
correct = set()
for i in range(len(rules)):
    potentials = calc(i, correct)
    if potentials is not None:
        correct.add(i)

print(correct)

# Calculate accumulator of fixed version

visited = set()
acc = 0
index = 0

while index not in visited:
    visited.add(index)
    ins, val = rules[index]

    if ins == 'acc':
        acc += val

    if ins == 'nop' and index + val in correct:
        rules[index] = ('jmp', val)
        print('Index', index, rules[index])
        break

    if ins == 'jmp' and index + 1 in correct:
        rules[index] = ('nop', val)
        print('Index', index, rules[index])
        break

    index += 1 if ins != 'jmp' else val


print(calc(0, set()))
