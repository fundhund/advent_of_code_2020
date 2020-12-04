with open("input.txt") as f:
    numbers = [int(line.rstrip('\n')) for line in f.readlines()]

found = False

for i in range(len(numbers)):
    if found:
        break
    first = numbers[i]
    second_candidates = []
    for j in range(len(numbers[i+1:])):
        if first + numbers[j] < 2020:
            second_candidates.append(numbers[j])
    for second in second_candidates:
        third = 2020-first-second
        if third in numbers:
            print(first, second, third, first * second * third)
            found = True
            break
