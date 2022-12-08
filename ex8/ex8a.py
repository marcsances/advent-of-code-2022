from typing import List


def visible_x(grid, row, col, rang):
    val = grid[row][col]
    # scan axis
    for c in rang:
        if grid[row][c] >= val:
            return False
    return True


def visible_y(grid, row, col, rang):
    val = grid[row][col]
    # scan axis
    for r in rang:
        if grid[r][col] >= val:
            return False
    return True


def count_interiors(grid: List[str]):
    ac = 0
    for row in range(1, len(grid) - 1):
        for col in range(1, len(grid[0]) - 1):
            if visible_x(grid, row, col, range(0, col)) or visible_x(grid, row, col, range(col+1, len(grid[0])))\
                    or visible_y(grid, row, col, range(0, row)) or visible_y(grid, row, col, range(row + 1, len(grid))):
                ac += 1
    return ac


def main():
    grid = []
    with open("input.txt", "r") as f:
        line = f.readline()
        while line != "":
            grid.append(line.strip())
            line = f.readline()
    height = len(grid)
    width = len(grid[0])
    edge = 2 * height + 2 * width - 4
    interiors = count_interiors(grid)
    print(edge + interiors)



if __name__ == "__main__":
    main()
