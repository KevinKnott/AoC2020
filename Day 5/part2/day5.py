import sys

testing = []

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

    testing.append(row * 8 + col)

testing.sort()

for i in range(1, len(testing)-1):
    # print(testing[i-1], testing[i], testing[i+1])
    # print((testing[i-1], (testing[i] - 1)), ((testing[i] + 1), testing[i+1]))
    if testing[i-1] != (testing[i] - 1):
        print(testing[i] - 1)
