with open("input.txt") as f:
    numbers = [int(line.rstrip('\n')) for line in f.readlines()]

for n in numbers:
    if 2020-n in numbers:
        print(n, 2020-n, n*(2020-n))
        break
