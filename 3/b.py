
def get_number_of_trees(right, down):
    r, c, trees_hit = 0, 0, 0

    while r < len(map):
        row = map[r]
        if row[c % len(row)] == '#':
            trees_hit += 1
        r += down
        c += right

    return trees_hit


with open("input.txt") as f:
    map = [row.rstrip('\n') for row in f.readlines()]

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

product_of_hit_trees = 1

for slope in slopes:
    product_of_hit_trees *= get_number_of_trees(*slope)

print(product_of_hit_trees)
