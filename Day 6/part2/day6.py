import sys

count = 0
cache = set()
reset = True

for value in sys.stdin.read().split("\n"):

    if value == "":
        count += len(cache)
        cache = set()
        reset = True

    else:
        currentPerson = set()
        for question in value:
            currentPerson.add(question)

        if reset == False:
            cache = cache & currentPerson
        else:
            cache = cache | currentPerson
            reset = False

count += len(cache)
print(count)
