from typing import List

def scan_top(grid, row, col):
    sc = 0
    for r in range(row - 1, -1, -1):
        if grid[r][col] >= grid[row][col]:
            return sc + 1
        sc = sc + 1
    return sc


def scan_left(grid, row, col):
    sc = 0
    for c in range(col - 1, -1, -1):
        if grid[row][c] >= grid[row][col]:
            return sc + 1
        sc = sc + 1
    return sc


def scan_bottom(grid, row, col):
    sc = 0
    for r in range(row + 1, len(grid)):
        if grid[r][col] >= grid[row][col]:
            return sc + 1
        sc = sc + 1
    return sc


def scan_right(grid, row, col):
    sc = 0
    for c in range(col + 1, len(grid[0])):
        if grid[row][c] >= grid[row][col]:
            return sc + 1
        sc = sc + 1
    return sc


def find_best(grid: List[str]):
    scores = list()
    ac = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            score_top = scan_top(grid, row, col)
            score_left = scan_left(grid, row, col)
            score_bottom = scan_bottom(grid, row, col)
            score_right = scan_right(grid, row, col)
            score = score_top * score_left * score_bottom * score_right
            scores.append(score)

    return sorted(scores, reverse=True)[0]


def main():
    grid = []
    with open("input.txt", "r") as f:
        line = f.readline()
        while line != "":
            grid.append(line.strip())
            line = f.readline()
    best = find_best(grid)
    print(best)



if __name__ == "__main__":
    main()
