import re

with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

number_of_valid_passwords = 0

for line in lines:
    matches = re.match(r'(\d{1,2})-(\d{1,2}) ([a-z]): ([a-z]+)', line)
    pos_1 = int(matches.group(1))-1
    pos_2 = int(matches.group(2))-1
    character = matches.group(3)
    password = matches.group(4)

    number_of_valid_passwords += (password[pos_1] ==
                                  character) != (password[pos_2] == character)

print(number_of_valid_passwords)
