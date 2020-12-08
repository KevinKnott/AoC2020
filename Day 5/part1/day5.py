import sys

maxSeatID = -float('inf')

for value in sys.stdin.read().split("\n"):
    # print(value)
    first = value[0:7]
    second = value[7:]

    left = 0
    right = 127

    for upperLower in first:
        if upperLower == 'F':
            right = (left + (right - left) // 2)
        else:
            left = (left + (right - left) // 2) + 1

    row = left if first[-1] == 'F' else right

    left = 0
    right = 7

    for upperLower in second:
        if upperLower == 'L':
            right = (left + (right - left) // 2)
        else:
            left = (left + (right - left) // 2) + 1

    col = left if second[-1] == 'L' else right

    maxSeatID = max(row * 8 + col, maxSeatID)

print(maxSeatID)
