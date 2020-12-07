import re

with open("input.txt") as f:
    paragraphs = f.read().split('\n\n')

passports = []

for p in paragraphs:
    passport = {}
    data = re.split('\n| ', p)
    for d in data:
        k, v = d.split(':')
        passport[k] = v
    passports.append(passport)

number_of_valid_passports = 0
required_keys = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']

for p in passports:
    number_of_valid_passports += all(k in p for k in required_keys)

print(number_of_valid_passports)
