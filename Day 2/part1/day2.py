import sys


def isValid(lower, upper, letter, password):
    numLetter = 0

    for cur in password:
        if cur == letter:
            numLetter += 1
            if numLetter > upper:
                return False

    return lower <= numLetter


count = 0
while True:
    try:
        numUses, letter, password = input().split(' ')

        lower, upper = map(int, numUses.split('-'))
        # print(lower, upper, letter[0], password)

        if isValid(lower, upper, letter[0], password):
            count += 1

    except EOFError:
        break


print(count)
