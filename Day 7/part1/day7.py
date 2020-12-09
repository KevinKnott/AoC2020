import sys

rules = [value.replace('.', '') for value in sys.stdin.read().split("\n")]

bagRules = {}

for rule in rules:
    cur = rule.split('contain')
    key = cur[0].split(' ')[0:2]
    key = " ".join(key)

    for bags in cur[1].split(','):

        if bags != ' no other bags':
            bags = bags.split(' ')
            numBags = bags[1]
            bagType = " ".join(bags[2:4])
            # print(numBags, bagType)
            if key not in bagRules:
                bagRules[key] = [(bagType, numBags)]
            else:
                bagRules[key].append((bagType, numBags))

            if bagType not in bagRules:
                bagRules[bagType] = []

    # print('next rule')

# for key in bagRules:
#     print(key, end=": ")
#     for value in bagRules[key]:
#         print(value, end=" ")
#     print()


def dfs(cur, visited, count, goal='shiny gold'):
    # print(cur)
    if count == 1:
        return 0
    if cur == goal:
        return 1

    for value in bagRules[cur]:
        if value[0] not in visited:
            visited.add(value[0])
            count += dfs(value[0], visited, count)

    return count


count = 0
for value in bagRules:
    if value == 'shiny gold':
        continue
    visited = set()
    count += dfs(value, visited, 0)
print(count)
