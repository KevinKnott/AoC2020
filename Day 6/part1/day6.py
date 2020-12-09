import sys

count = 0
cache = set()

for value in sys.stdin.read().split("\n"):

    if value == "":
        count += len(cache)
        cache = set()

    else:
        for question in value:
            if question not in cache:
                cache.add(question)

count += len(cache)
print(count)
