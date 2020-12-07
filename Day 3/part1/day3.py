import sys

treeCount = 0
column = 0

while True:
    try:
        row = input()
        print(row, column, row[column] == '#')

        if row[column] == '#':
            treeCount += 1

        column = (column + 3) % (len(row))

    except EOFError:
        break

print(treeCount)
