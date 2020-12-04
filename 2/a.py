import re

with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

number_of_valid_passwords = 0

for line in lines:
    matches = re.match(r'(\d{1,2})-(\d{1,2}) ([a-z]): ([a-z]+)', line)
    min = int(matches.group(1))
    max = int(matches.group(2))
    character = matches.group(3)
    password = matches.group(4)

    number_of_valid_passwords += min <= password.count(character) <= max

print(number_of_valid_passwords)
