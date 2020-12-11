import sys
from collections import deque

values = [int(value) for value in sys.stdin.read().split("\n")]


def findFirstOff():
    for target in range(26, len(values)):
        found = False
        seen = set()

        for x in range(target - 26, target):
            realTarget = values[target] - values[x]

            if realTarget in seen:
                found = True
                continue

            seen.add(values[x])

        if not found:
            return(values[target])

    return None


print(findFirstOff())
