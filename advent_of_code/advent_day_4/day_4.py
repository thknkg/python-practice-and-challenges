"""check which pairs have one of the pair fully enveloped in the other"""

with open(r"C:\Users\micah\PycharmProjects\python-practice-and-challenges\advent_of_code\advent_day_4\day_4.txt") as f:
    lines = [line.rstrip() for line in f]

count = 0
any_count = 0


def check_overlap(pairs):
    """compare high and low vals to see if it applies"""
    if int(pairs[0][0]) <= int(pairs[1][0]) and int(pairs[0][1]) >= int(pairs[1][1]):
        return True

    elif int(pairs[0][0]) >= int(pairs[1][0]) and int(pairs[0][1]) <= int(pairs[1][1]):
        return True

    else:
        return False


def check_any_overlap(pairs):
    """compare high and low vals to see if it applies"""
    if int(pairs[0][0]) <= int(pairs[1][0]):
        if int(pairs[0][1]) >= int(pairs[1][0]):
            return True

    elif int(pairs[1][0]) <= int(pairs[0][0]):
        if int(pairs[1][1]) >= int(pairs[0][0]):
            return True

    elif int(pairs[0][1]) >= int(pairs[1][1]):
        if int(pairs[0][0]) <= int(pairs[1][1]):
            return True

    elif int(pairs[1][1]) >= int(pairs[0][1]):
        if int(pairs[1][0]) <= int(pairs[0][1]):
            return True

    else:
        return False


for line in lines:
    # splitting neatly
    split = line.split(',')
    split_list = []

    for vals in split:
        pair = vals.split('-')
        split_list.append(pair)

    # iterate function over each pair
    if check_overlap(split_list):
        count += 1

    if check_any_overlap(split_list):
        any_count += 1

print(count)
print(any_count)
