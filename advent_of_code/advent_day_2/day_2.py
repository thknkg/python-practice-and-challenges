"""calc rps game score and output total"""


def calc_score():
    score = 0

    for line in open(r"/advent_of_code/advent_day_2/day_2.txt"):
        line = line.split()

        opponent = line[0]
        player = line[1]

        match player:
            # rock
            case "X":
                score += 1
                match opponent:

                    # rock
                    case "A":
                        score += 3

                    # paper
                    case "B":
                        score += 0

                    # scissors
                    case "C":
                        score += 6

            # paper
            case "Y":
                score += 2
                match opponent:

                    # rock
                    case "A":
                        score += 6

                    # paper
                    case "B":
                        score += 3

                    # scissors
                    case "C":
                        score += 0

            # scissors
            case "Z":
                score += 3
                match opponent:

                    # rock
                    case "A":
                        score += 0

                    # paper
                    case "B":
                        score += 6

                    # scissors
                    case "C":
                        score += 3

    print(score)


def calc_score_from_result():
    score = 0
    rock = 1
    paper = 2
    scissors = 3
    lose = 0
    draw = 3
    win = 6

    for line in open(r"/advent_of_code/advent_day_2/day_2.txt"):
        line = line.split()

        opponent = line[0]
        player = line[1]

        match player:
            # lose
            case "X":
                score += lose
                match opponent:
                    # rock
                    case "A":
                        score += scissors
                    # paper
                    case "B":
                        score += rock
                    # scissors
                    case "C":
                        score += paper

                        # draw
            case "Y":
                score += draw
                match opponent:

                    # rock
                    case "A":
                        score += rock

                    # paper
                    case "B":
                        score += paper

                    # scissors
                    case "C":
                        score += scissors

            # win
            case "Z":
                score += win
                match opponent:

                    # rock
                    case "A":
                        score += paper

                    # paper
                    case "B":
                        score += scissors

                    # scissors
                    case "C":
                        score += rock

    print(score)


calc_score()
calc_score_from_result()
