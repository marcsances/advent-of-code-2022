from typing import Generator


def find_unique(rs1, rs2):
    for chr in rs1:
        if chr in rs2:
            return chr
    return None


def get_items() -> Generator[str, None, None]:
    with open("input.txt", "r") as f:
        for line in f.readlines():
            rs1 = line[:int(len(line)/2)].strip()
            rs2 = line[int(len(line)/2):].strip()
            item = find_unique(rs1, rs2)
            if item:
                priority = ord(item) - ord('A') + 27 if item.isupper() else ord(item) - ord('a') + 1
                yield priority
            else:
                yield 0


def main():
    print(sum(get_items()))


if __name__ == "__main__":
    main()
