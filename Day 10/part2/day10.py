import sys
from collections import deque

values = [int(value) for value in sys.stdin.read().split("\n")]
values.sort()


def findHighestJoltage():
    joltage = 0
    index = 0
    diff = [0, 0, 0]

    while index < len(values):
        curDif = (values[index] - joltage)
        if curDif <= 3:
            diff[curDif-1] += 1
            joltage = values[index]
            index += 1
        else:
            break

    # The plus one is part of the instructions you go up plus 3 at the end
    return (joltage, diff[0] * (diff[2]+1))


joltage, answer = findHighestJoltage()
print(joltage, answer)


count = {0: 1}
maxVal = -float('inf')
for val in values:
    count[val] = 0
    maxVal = max(maxVal, val)
    # print(maxVal, count)
    if val - 1 in count:
        count[val] += count[val-1]
    if val - 2 in count:
        count[val] += count[val-2]
    if val - 3 in count:
        count[val] += count[val-3]

    if val == joltage:
        break

print(count[maxVal])
