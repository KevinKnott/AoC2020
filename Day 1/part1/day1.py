import sys
cache = set()
goal = 2020

while True:
    try:
        curNum = int(input())

        if curNum not in cache:
            cache.add(curNum)

        target = goal - curNum
        if target in cache:
            print(curNum, target, (curNum * target))

    except EOFError:
        break
