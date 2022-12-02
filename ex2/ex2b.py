def find_play_score(him, expected_result):
    if expected_result == "X":
        return {"A": 3, "B": 1, "C": 2}[him]
    elif expected_result == "Y":
        return {"A": 1, "B": 2, "C": 3}[him]
    else:
        return {"A": 2, "B": 3, "C": 1}[him]


def get_result_score(result):
    return {"X": 0, "Y": 3, "Z": 6}[result]


def main():
    with open("input.txt", "r") as f:
        score = 0
        for line in f.readlines():
            print("Play " + line)
            him = line[0]
            expected_result = line[2]
            score += find_play_score(him, expected_result)
            score += get_result_score(expected_result)
            print("Current score " + str(score))
    print("Final score " + str(score))


if __name__ == "__main__":
    main()