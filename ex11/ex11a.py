import math
from functools import reduce
from typing import List, Tuple, Dict

ROUNDS = 20


class Monkey:

    def __init__(self, starting_items: List[int], operation: str, test_by: int, monkey_if_true: int,
                 monkey_if_false: int):
        self.items = starting_items
        self.operation = operation
        self.test_by = test_by
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.business = 0

    def cycle(self) -> List[Tuple[int, int]]:
        throws = []
        for item in self.items:
            self.business += 1
            op = self.operation.replace("old", str(item))
            worry = item
            if "+" in op:
                o1, o2 = op.split(" + ")
                worry = math.floor(float(int(o1) + int(o2)) / 3.0)
            elif "*" in op:
                o1, o2 = op.split(" * ")
                worry = math.floor(float(int(o1) * int(o2)) / 3.0)
            throw_to = self.monkey_if_true if worry % self.test_by == 0 else self.monkey_if_false
            throws.append((throw_to, worry))
        # All items inspected and send to deliver, empty monkey items
        self.items = []
        return throws


class MonkeyBuilder:

    def __init__(self, index: int):
        self.index = index
        self.starting_items = None
        self.operation = None
        self.test_by = None
        self.monkey_if_true = None
        self.monkey_if_false = None

    def set_starting_items(self, starting_items: List[int]):
        self.starting_items = starting_items

    def set_operation(self, operation: str):
        self.operation = operation

    def set_test_by(self, test_by: int):
        self.test_by = test_by

    def set_monkey_if_true(self, monkey_if_true: int):
        self.monkey_if_true = monkey_if_true

    def set_monkey_if_false(self, monkey_if_false: int):
        self.monkey_if_false = monkey_if_false

    def build(self) -> Tuple[int, Monkey]:
        for it in self.__dict__.values():
            if it is None:
                raise ValueError("All attributes must be set")
        return (self.index, Monkey(self.starting_items, self.operation, self.test_by, self.monkey_if_true,
                                   self.monkey_if_false))


def get_lines(f):
    line = f.readline()
    while line != "":
        yield line.strip()
        line = f.readline()


def main():
    cur_monkey = MonkeyBuilder(0)
    monkeys: Dict[int, Monkey] = {}
    nmonkeys = 0
    with open("input.txt", "r") as f:
        for line in get_lines(f):
            if line.startswith("Monkey"):
                cur_monkey = MonkeyBuilder(int(line.split(":")[0].split(" ")[1]))
            elif line.startswith("Starting items:"):
                cur_monkey.set_starting_items(list(map(lambda s: int(s.strip()),
                                                       line.replace("Starting items: ", "").split(","))))
            elif line.startswith("Operation:"):
                cur_monkey.set_operation(line.replace("Operation: new = ", ""))
            elif line.startswith("Test: "):
                cur_monkey.set_test_by(int(line.replace("Test: divisible by ", "").strip()))
            elif line.startswith("If true:"):
                cur_monkey.set_monkey_if_true(int(line.replace("If true: throw to monkey ", "").strip()))
            elif line.startswith("If false:"):
                cur_monkey.set_monkey_if_false(int(line.replace("If false: throw to monkey ", "").strip()))
            elif line == "":
                idx, monkey = cur_monkey.build()
                nmonkeys += 1
                monkeys[idx] = monkey

    idx, monkey = cur_monkey.build()
    if idx not in monkeys:
        # EOF
        nmonkeys += 1
        monkeys[idx] = monkey

    for _ in range(ROUNDS):
        for monkey in range(nmonkeys):
            throws = monkeys[monkey].cycle()
            for throw_to, worry in throws:
                monkeys[throw_to].items.append(worry)

    for idx, monkey in monkeys.items():
        print("Monkey " + str(idx) + " inspected items " + str(monkey.business) + " times.")

    print("Level of monkey business: " +
          str(reduce(lambda a1, a2: a1 * a2,
                     sorted(map(lambda mk: mk.business, monkeys.values()), reverse=True)[:2])))


if __name__ == "__main__":
    main()