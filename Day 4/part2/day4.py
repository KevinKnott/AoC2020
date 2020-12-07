import sys
import re

validation = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: (x.endswith("cm") and 150 <= int(x[:-2]) <= 193) or
    (x.endswith("in") and 59 <= int(x[:-2]) <= 76),
    "hcl": lambda x: re.fullmatch(r"#[\da-f]{6}", x),
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: re.fullmatch(r"\d{9}", x),
    "cid": lambda x: True
}

# (Birth Year)
# (Issue Year)
# (Expiration Year)
# (Height)
# (Hair Color)
# (Eye Color)
# (Passport ID)
# (Country ID)
count = 0

cache = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}

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
        for temp in value.split(' '):
            key, value = temp.split(':')
            if validation[key](value):
                cache.discard(key)


if len(cache) == 0:
    count += 1

if len(cache) == 1 and "cid" in cache:
    count += 1

print(count)
