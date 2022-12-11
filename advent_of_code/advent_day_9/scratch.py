"""original implementation of the day_9 before reorienting it a bit
head_grid = {0, 0}
tail_grid = {0, 0}

text = [i.split(" ") for i in open("day_9.txt").read().strip().split("\n")]
head = [0, 0]
tail = [0, 0]

for direction in text:
    prev_tail = (tail[0], tail[1])
    new_head = (head[0], head[1])
    new_tail = (tail[0], tail[1])
    direct = direction[0]
    amount = int(direction[1])
    #
    # print(head, 'head')
    # update head coordinates for each direction
    match direct:
        case "U":
            #update with new coordinates
            new_head = (head[0], head[1] + amount)
            head[1] += amount

            # head is above, move tail one below it
            # if new_head[1] - tail[1] > 1:
            #     new_tail = (tail[0], new_head[1] - 1)
            #     tail[1] += amount - 1


        case "D":
            new_head = (head[0], head[1] - amount)

            head[1] -= amount
            # if new_head[1] - tail[1] < 1:
            #     new_tail = (tail[0], new_head[1] + 1)
            #     tail[1] -= amount - 1

        case "L":
            new_head = (head[0] - amount, head[1])
            head[0] -= amount
            # if abs(new_head[0]) - abs(tail[0]) > 1:
            #     new_tail = (new_head[0] + 1, tail[1])
            #     tail[0] -= amount - 1



        case "R":
            new_head = (head[0] + amount, head[1])
            head[0] += amount
            # if new_head[0] - tail[0] < 1:
            #     new_tail = (new_head[0] - 1, tail[1])
            #     tail[0] += amount - 1

    # print(new_head, 'new head')
    # print(tail, 'tail')

    if len(range(new_head[0], tail[0])) > 1:
        tail[0] -= amount
        new_tail = (tail[0], tail[1])

    elif len(range(tail[0], new_head[0])) > 1:
        # print(new_head, tail)
        # print(len(range(tail[0], new_head[0])))
        tail[0] += amount
        new_tail = (tail[0], tail[1])

    if len(range(new_head[1], tail[1])) > 1:
        tail[1] -= amount
        new_tail = (tail[0], tail[1])

    elif len(range(tail[1], new_head[1])) > 1:
        tail[1] += amount
        new_tail = (tail[0], tail[1])
    print(prev_tail, new_tail)
    for i in range(prev_tail[0], new_tail[0]):
        for j in range(prev_tail[1], new_tail[1]):
            x = (i, j)
            tail_grid.add(x)

    # print(tail, 'tail after')
    # print(new_tail, 'new tail')
    # print(head, 'final head')
    # print()
    head_grid.add(new_head)
    tail_grid.add(new_tail)


print(len(tail_grid))

"""