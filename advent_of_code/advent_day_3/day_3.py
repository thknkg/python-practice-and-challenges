"""Find the item type that appears in both compartments of each rucksack, and get the sum"""

with open(r"C:\Users\micah\PycharmProjects\python-practice-and-challenges\advent_of_code\advent_day_3\day_3.txt") as f:
    lines = [line.rstrip() for line in f]

item_priority_sum = 0

for line in lines:
    # split in half
    compartment_one, compartment_two = line[:len(line)//2], line[len(line)//2:]

    # iterate through
    for letter in compartment_one:
        if letter in compartment_two:
            # note location of character
            index = compartment_two.index(letter)

            # convert to requested values
            if 97 <= ord(letter) <= 122:
                item_priority_sum += (ord(letter) - 96)

            elif 65 <= ord(letter) <= 90:
                item_priority_sum += (ord(letter) - 38)

            # remake compartment two to prevent having 2 in comp 1 and adding a single value from comp 2 twice
            compartment_two = compartment_two[:index]

print(item_priority_sum)


count = 0
badge_priority_sum = 0

for line in lines:
    # add to set
    if count == 0:
        set_one = set(line)
    elif count == 1:
        set_two = set(line)
    elif count == 2:
        set_three = set(line)

    count += 1

    if count == 3:
        #### using set ####
        # find intersection in set
        common_value = set_one.intersection(set_two, set_three)
        for val in common_value:
            if 97 <= ord(val) <= 122:
                badge_priority_sum += ord(val) - 96
            else:
                badge_priority_sum += ord(val) - 38
        count = 0

print(badge_priority_sum)
