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
    return diff[0] * (diff[2]+1)


answer = findHighestJoltage()
print(answer)
