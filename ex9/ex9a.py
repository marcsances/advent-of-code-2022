def instructions(f):
    line = f.readline()
    while line != "":
        yield line
        line = f.readline()


def move(head, tail, direction):
    if direction == "R":
        head = (head[0], head[1] + 1)
        # If the tail is two columns behind the head, it will always end before the head
        # Rest of cases are a no op
        if tail[1] == head[1] - 2:
            tail = (head[0], head[1] - 1)
    elif direction == "L":
        head = (head[0], head[1] - 1)
        # If the tail is two columns on top the head, it will always end after the head
        # Rest of cases are a no op
        if tail[1] == head[1] + 2:
            tail = (head[0], head[1] + 1)
    elif direction == "U":
        head = (head[0] - 1, head[1])
        if tail[0] == head[0] - 2:
            tail = (head[0] + 1, head[1])
    elif direction == "D":
        head = (head[0] + 1, head[1])
        if tail[0] == head[0] + 2:
            tail = (head[0] - 1, head[1])
    return head, tail

def move_old(head, tail, direction):
    if direction == "R":
        head = (head[0], head[1] + 1)
        if tail[0] == head[0]:
            if tail[1] == head[1] - 2:
                # head two steps from tail, keep up
                tail = (head[0], head[1] - 1)
            elif tail[1] == head[1] - 1:
                # head was overlapped with tail, now it's on its right. no op
                pass
            elif tail[1] == head[1]:
                # head overlapped with tail now, no op
                pass
            else:
                raise ValueError("some illegal state")
        elif tail[0] == head[0] - 1 or tail[0] == head[0] + 1:
            # head was diagonal upwards and now is moving right, move diagonally
            tail = (head[0], head[1] - 1)
    elif direction == "L":
        head = (head[0], head[1] - 1)
        if tail[0] == head[0]:
            if tail[1] == head[1] + 2:
                # head two steps from tail, keep up
                tail = (head[0], head[1] + 1)
            elif tail[1] == head[1] + 1:
                # head was overlapped with tail, now it's on its right. no op
                pass
            elif tail[1] == head[1]:
                # head overlapped with tail now, no op
                pass
            else:
                raise ValueError("some illegal state")
        elif tail[0] == head[0] - 1 or tail[0] == head[0] + 1:
            # head was diagonal upwards and now is moving left, move diagonally
            tail = (head[0], head[1] + 1)
    elif direction == "U":
        head = (head[0] - 1, head[1])
        if tail[1] == head[1]:
            if tail[0] == head[0] + 2:
                tail = (head[0] - 1, head[1])
            elif tail[0] == head[0] + 1:
                pass
            elif tail[0] == head[0]:
                pass
            else:
                raise ValueError("some illegal state")
        elif tail[1] == head[1] - 1 or tail[1] == head[1] + 1:
            if tail[0] == head[0] + 2:
                # move diagonally
                tail = (head[0] - 1, head[1])
    elif direction == "D":
        head = (head[0] + 1, head[1])
        if tail[1] == head[1]:
            if tail[0] == head[0] - 2:
                tail = (head[0] + 1, head[1])
            elif tail[0] == head[0] - 1:
                pass
            elif tail[0] == head[0]:
                pass
            else:
                raise ValueError("some illegal state")
        elif tail[1] == head[1] - 1 or tail[1] == head[1] + 1:
            if tail[0] == head[0] - 2:
                # move diagonally
                tail = (head[0] + 1, head[1])
    return head, tail


def main():
    # row, col
    head = (0, 0)
    tail = (0, 0)
    visited = {(0, 0)}
    with open("input.txt", "r") as f:
        for instruction in instructions(f):
            direction, repeat = instruction.split(" ")
            for _ in range(int(repeat)):
                print("move " + direction)
                head, tail = move(head, tail, direction)
                visited.add(tail)
                print("Tail is at " + str(tail) + " and head is at " + str(head))
                print("Visited positions: " + str(visited))

    print(len(visited))


if __name__ == "__main__":
    main()