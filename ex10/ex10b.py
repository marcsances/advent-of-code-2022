import sys

def get_lines(f):
    line = f.readline()
    while line != "":
        yield line
        line = f.readline()


def draw(cycle, xreg):
    if (cycle - 1) % 40 in (xreg - 1, xreg + 1, xreg):
        sys.stdout.write("█")
    else:
        sys.stdout.write(" ")
    if (cycle - 1) % 40 == 39:
        sys.stdout.write("\n")


def main():
    xreg = 1
    cycle = 1
    with open("input.txt", "r") as f:
        for instruction in get_lines(f):
            if instruction.startswith("addx"):
                draw(cycle, xreg)
                cycle += 1
                draw(cycle, xreg)
                cycle += 1
                xreg += int(instruction.replace("addx ", ""))
            else:
                draw(cycle, xreg)
                cycle += 1



if __name__ == "__main__":
    main()