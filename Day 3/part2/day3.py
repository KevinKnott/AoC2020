import sys

treeCount = [0] * 5
columns = [0] * 5
lineNum = 1

while True:
    try:
        row = input()
        lineNum += 1

        #  Count all but slope of 2
        for i in range(len(treeCount) - 1):
            if row[columns[i]] == '#':
                treeCount[i] += 1

            columns[i] = (columns[i] + (i * 2 + 1)) % len(row)

        if lineNum % 2 == 0:
            if row[columns[4]] == '#':
                treeCount[4] += 1

            columns[4] = (columns[4] + 1) % len(row)

        print(columns)
    except EOFError:
        break

cumMult = 1
for x in treeCount:
    cumMult *= x

print(treeCount, cumMult)
# 6050183040
# 4950149760
