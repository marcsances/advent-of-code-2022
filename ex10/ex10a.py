def get_lines(f):
    line = f.readline()
    while line != "":
        yield line
        line = f.readline()


def check_cycle(cycle, xreg, signals):
    if cycle in [20, 60, 100, 140, 180, 220]:
        signals.append(cycle * xreg)


def main():
    xreg = 1
    cycle = 1
    signals = []
    with open("input.txt", "r") as f:
        for instruction in get_lines(f):
            if instruction.startswith("addx"):
                cycle += 1
                check_cycle(cycle, xreg, signals)
                xreg += int(instruction.replace("addx ", ""))
            cycle += 1
            check_cycle(cycle, xreg, signals)
    print(sum(signals))



if __name__ == "__main__":
    main()