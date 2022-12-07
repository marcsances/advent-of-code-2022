def generate_rows(f):
    for line in f.readlines():
        yield line


def print_crates(crates):
    for k in sorted(crates.keys()):
        print("%d -> %s" % (k, ",".join(crates[k])))


def gen_crates(crates, gen):
    for line in gen:
        for idx, i in enumerate(range(1, len(line), 4)):
            if line[i].isdigit():
                next(gen)  # skip blank line
                return
            if line[i] != " ":
                if idx + 1 not in crates:
                    crates[idx + 1] = list()
                crates[idx + 1].append(line[i])


def rev(l):
    r = l[:]
    r.reverse()
    return r


def main():
    crates = dict()
    with open("input.txt", "r") as f:
        gen = generate_rows(f)
        gen_crates(crates, gen)
        print_crates(crates)
        for line in gen:
            print(line.strip())
            l = line.replace("move ", "").replace(" from ", ",").replace(" to ", ",")
            qty, src, dest = map(lambda x: int(x), l.split(","))
            crates[dest] = rev(crates[src][:qty]) + crates[dest]
            crates[src] = crates[src][qty:]
            print_crates(crates)

if __name__ == "__main__":
    main()
