from typing import Dict, Tuple


def get_lines(f):
    line = f.readline()
    while line != "":
        yield line
        line = f.readline()

def main():
    grid: Dict[Tuple[int, int], str] = dict()
    abyss_y = 0
    with open("input.txt", "r") as f:
        for line in get_lines(f):
            last_x, last_y = None, None
            for rock in map(lambda r: r.strip(), line.split("->")):
                x, y = map(lambda s: int(s), rock.split(","))
                if last_x is not None and last_y is not None:
                    if last_x == x:
                        for pen_y in range(last_y if last_y < y else y, y if last_y < y else last_y):
                            grid[x, pen_y] = "#"
                            abyss_y = max(abyss_y, pen_y)
                    elif last_y == y:
                        for pen_x in range(last_x if last_x < x else x, x if last_x < x else last_x):
                            grid[pen_x, y] = "#"
                grid[x, y] = "#"
                abyss_y = max(abyss_y, y)
                last_x = x
                last_y = y
    drops = 0
    end = False
    while not end:
        sand_x, sand_y = 500, 0
        stationary = False
        while not stationary and not end:
            if (sand_x, sand_y + 1) not in grid and sand_y + 1 < 2 + abyss_y:
                # fall down
                sand_y = sand_y + 1
            elif (sand_x - 1, sand_y + 1) not in grid and sand_y + 1 < 2 + abyss_y:
                # fall to left
                sand_x = sand_x - 1
                sand_y = sand_y + 1
            elif (sand_x + 1, sand_y + 1) not in grid and sand_y + 1 < 2 + abyss_y:
                # fall to right
                sand_x = sand_x + 1
                sand_y = sand_y + 1
            else:
                grid[sand_x, sand_y] = "o"
                drops = drops + 1
                stationary = True
                if sand_x == 500 and sand_y == 0:
                    end = True
    print(drops)



if __name__ == "__main__":
    main()