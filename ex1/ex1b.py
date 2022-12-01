def main():
    ac = 0
    largestA, largestB, largestC = 0, 0, 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                ac += int(line)
                continue
            if ac > largestA:
                largestC = largestB
                largestB = largestA
                largestA = ac
            elif ac > largestB:
                largestC = largestB
                largestB = ac
            elif ac > largestC:
                largestC = ac
            ac = 0
    print(largestA + largestB + largestC)


if __name__ == "__main__":
    main()
