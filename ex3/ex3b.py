from typing import Generator


def get_common() -> Generator[int, None, None]:
    with open("input.txt", "r") as f:
        buf = []
        for line in f.readlines():
            buf.append(set(line.strip()))
            if len(buf) == 3:
                common = list(buf[0].intersection(buf[1]).intersection(buf[2]))[0]
                priority = ord(common) - ord('A') + 27 if common.isupper() else ord(common) - ord('a') + 1
                yield priority
                buf = []


def main():
    print(sum(get_common()))


if __name__ == "__main__":
    main()
