def contained(range1, range2):
    s1, e1 = list(map(lambda x: int(x), range1.strip().split('-')))
    s2, e2 = list(map(lambda x: int(x), range2.strip().split('-')))
    return (s1 <= s2 and e1 >= e2) or (s2 <= s1 and e2 >= e1)

def main():
    with open("input.txt", "r") as f:
        ac = 0
        for line in f.readlines():
            range1, range2 = line.strip().split(',')
            if contained(range1, range2):
                print("contained " + line)
                ac += 1
    print(ac)


if __name__ == "__main__":
    main()
