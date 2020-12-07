import sys


def isValid(first, second, letter, password):
    if len(password) < first:
        return False

    first = password[first] == letter
    second = password[second] == letter

    return first ^ second


count = 0
while True:
    try:
        positions, letter, password = input().split(' ')

        first, second = map(int, positions.split('-'))
        # print(first, second, letter[0], password)

        # The minus 1 is for indexing starting at 0
        if isValid(first - 1, second - 1, letter[0], password):
            count += 1

    except EOFError:
        break


print(count)
