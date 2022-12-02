def did_i_win(him, me):
    return (him == "A" and me == "Y") or (him == "B" and me == "Z") or (him == "C" and me == "X")


def main():
    with open("input.txt", "r") as f:
        score = 0
        for line in f.readlines():
            print("Play " + line)
            him = line[0]
            me = line[2]
            score += int(ord(me) - ord('W'))
            print("Figure score " + str(int(ord(me) - ord('W'))))
            if did_i_win(him, me):
                score += 6
                print("I won +6")
            elif ord(him) - ord("A") == ord(me) - ord("X"):
                score += 3
                print("Draw +3")
            print("Current score " + str(score))
    print("Final score " + str(score))


if __name__ == "__main__":
    main()