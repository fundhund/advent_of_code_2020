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

is_valid = {
    'byr': (lambda year:   1920 <= int(year) <= 2002 if year.isdigit() else False),
    'iyr': (lambda year:   2010 <= int(year) <= 2020 if year.isdigit() else False),
    'eyr': (lambda year:   2020 <= int(year) <= 2030 if year.isdigit() else False),
    'hgt': (lambda height: (150 <= int(height[0:-2]) <= 193 if height[-2:] == 'cm' else (59 <= int(height[0:-2]) <= 76 if height[-2:] == 'in' else False)) if height[0:-2].isdigit() else False),
    'hcl': (lambda color:  bool(re.match(r'^#[0-9a-f]{6}$', color))),
    'ecl': (lambda color:  color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
    'pid': (lambda id:     bool(re.match(r'^\d{9}$', id))),
}


def is_passport_complete(p): return all(k in p for k in required_keys)


def is_passport_valid(p): return all(
    is_valid[k](p[k]) for k in required_keys)


for p in passports:
    number_of_valid_passports += (is_passport_complete(p)
                                  and is_passport_valid(p))

print(number_of_valid_passports)
