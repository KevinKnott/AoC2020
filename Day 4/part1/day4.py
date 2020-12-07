import sys

cache = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

# (Birth Year)
# (Issue Year)
# (Expiration Year)
# (Height)
# (Hair Color)
# (Eye Color)
# (Passport ID)
# (Country ID)
count = 0

for value in sys.stdin.read().split("\n"):
    # print(value)
    if value == '':
        if len(cache) == 0:
            count += 1

        if len(cache) == 1 and "cid" in cache:
            count += 1

        cache = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
    else:
        # print(value)
        for key in value.split(' '):
            cache.discard(key.split(':')[0])


if len(cache) == 0:
    count += 1

if len(cache) == 1 and "cid" in cache:
    count += 1

print(count)
