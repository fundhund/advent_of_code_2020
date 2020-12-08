with open("input.txt") as f:
    boarding_passes = [row.rstrip('\n') for row in f.readlines()]


def get_row(boarding_pass):
    row = 0
    for i in range(7):
        if boarding_pass[i] == "B":
            row += 2**(6-i)
    return row


def get_column(boarding_pass):
    column = 0
    for i in range(3):
        if boarding_pass[-3+i] == "R":
            column += 2**(2-i)
    return column


def get_id(boarding_pass):
    return get_row(boarding_pass) * 8 + get_column(boarding_pass)


def is_neither_very_front_nor_very_back(boarding_pass):
    return not boarding_pass.startswith(("FFFFFFF", "BBBBBBB"))


*boarding_pass_ids, = sorted(map(get_id,
                                 filter(is_neither_very_front_nor_very_back, boarding_passes)))

for my_id in range(1, 908):
    if my_id not in boarding_pass_ids and my_id - 1 in boarding_pass_ids and my_id + 1 in boarding_pass_ids:
        break

print(my_id)
