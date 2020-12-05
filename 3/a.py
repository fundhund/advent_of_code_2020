# right 3, down 1

with open("input.txt") as f:
    map = [row.rstrip('\n') for row in f.readlines()]

r, c, trees_hit = 0, 0, 0

while r < len(map):
    row = map[r]
    if row[c % len(row)] == '#':
        trees_hit += 1
    r += 1
    c += 3

print(trees_hit)
