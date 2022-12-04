def overlapped(range1, range2):
    s1, e1 = list(map(lambda x: int(x), range1.strip().split('-')))
    s2, e2 = list(map(lambda x: int(x), range2.strip().split('-')))
    return len(set(range(s1, e1 + 1)).intersection(set(range(s2, e2 + 1)))) > 0

def main():
    with open("input.txt", "r") as f:
        ac = 0
        for line in f.readlines():
            range1, range2 = line.strip().split(',')
            if overlapped(range1, range2):
                print("overlapped " + line)
                ac += 1
    print(ac)


if __name__ == "__main__":
    main()
