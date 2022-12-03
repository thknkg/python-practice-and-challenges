"""add calories each elf carries, and determine the total the top 3 are carrying"""
with open(r"C:\Users\micah\PycharmProjects\Practice_Projects\advent_day_1\day_1.txt") as f:
    lines = [line.rstrip() for line in f]
sum = 0
sum_2 = 0
sum_3 = 0
temp_sum = 0
temp_sum_2 = 0
temp_sum_3 = 0
count = 1
num_elf = 0
final = []

# iterate over text file
for i in lines:
    # newline indicates new person
    if i == "":

        # running list for debugging
        final.append(temp_sum)

        # if bigger than third biggest sum
        if temp_sum > sum_3:

            # if bigger than second biggest sum
            if temp_sum > sum_2:

                # if bigger than biggest sum
                if temp_sum > sum:
                    # cycle the previous values down
                    sum_3 = sum_2
                    sum_2 = sum
                    sum = temp_sum

                else:
                    # cycle the previous values down
                    sum_3 = sum_2
                    sum_2 = temp_sum


            else:
                sum_3 = temp_sum


        else:
            pass

        temp_sum = 0

    else:
        try:
            temp_sum += int(i)
        except ValueError:
            continue



# print(sorted(final, reverse=True))

print(sum, sum_2, sum_3)
print(sum + sum_2 + sum_3)
