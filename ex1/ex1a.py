def main():
    ac = 0
    largest = 0
    with open("input.txt", "r") as f:
        for line in f.readlines():
            if len(line.strip()) > 0:
                ac += int(line)
                continue
            if ac > largest:
                largest = ac
            ac = 0
    print(largest)


if __name__ == "__main__":
    main()
