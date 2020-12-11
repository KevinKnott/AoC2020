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


def findSubArraySum(target):
    left, right = 0, 1
    curSum = values[left] + values[right]

    while right < len(values):
        if left == right:
            right += 1
            curSum += values[right]

        if curSum > target:
            curSum -= values[left]
            left += 1
        elif curSum < target:
            right += 1
            curSum += values[right]
        else:
            return (left, right)


sumToLookFor = findFirstOff()
print(sumToLookFor)

left, right = findSubArraySum(sumToLookFor)

small, large = float('inf'), -float('inf')
for i in range(left, right+1):
    small = min(small, values[i])
    large = max(large, values[i])

print(left, right, small+large)
