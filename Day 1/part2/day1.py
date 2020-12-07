import sys
values = []
goal = 2020

while True:
    try:
        curNum = int(input())

        values.append(curNum)

    except EOFError:
        break


values.sort()


def threeNumSum(values):
    for i in range(len(values)):
        left = i + 1
        right = len(values) - 1

        while left <= right:
            print(values[i], values[left], values[right])

            if values[i] + values[left] + values[right] < goal:
                left += 1
            elif values[i] + values[left] + values[right] > goal:
                right -= 1
            else:
                return (values[i], values[left], values[right], (values[i] * values[left] * values[right]))


print(threeNumSum(values))
