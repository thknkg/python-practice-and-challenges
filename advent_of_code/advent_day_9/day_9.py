"""determine how many positions the tail of the rope visits at least one time"""
text = [i.split(" ") for i in open("day_9.txt").read().strip().split("\n")]
body = [0] * 10

# list of sets for each part of rope, so that uniquely visited locations can be tracked
locations = [{x} for x in body]

# i was originally using x and y coordinates but someone utilized complex numbers, so I reformatted it to that style
imag_num = {"U": -1j, "D": +1j, "L": +1, "R": -1}

for direction in text:
    direct = direction[0]
    amount = int(direction[1])
    for _ in range(amount):
        body[0] += imag_num[direct]

        for i in range(1, 10):
            distance = body[i - 1] - body[i]

            # if the distance is too far
            if abs(distance) >= 2:

                # split by real and imaginary
                body[i] += complex((distance.real > 0) - (distance.real < 0), (distance.imag > 0) - (distance.imag < 0))

                # add to set
                locations[i].add(body[i])

print(len(locations[1]), len(locations[9]))
