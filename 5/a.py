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


print(max(map(get_id, boarding_passes)))
