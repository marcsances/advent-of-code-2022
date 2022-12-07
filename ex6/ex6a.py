import sys
from enum import Enum
from typing import List, Dict


class NodeType(Enum):
    DIRECTORY = 0
    FILE = 1


class Node:
    def __init__(self, name: str, type: NodeType, children: Dict[str, 'Node'], size: int):
        self.name = name
        self.type = type
        self.children = children
        self.size = size


def genlines(f):
    for line in f.readlines():
        yield line.strip()
    yield None


def get_node(rootNode: Node, cwd: str):
    if cwd == "":
        return rootNode
    cur_node = rootNode
    for node_name in cwd.split("/"):
        if node_name == "":
            return cur_node
        cur_node = cur_node.children[node_name]
    return cur_node


def get_size(node: Node, large_ones: List[Node]) -> int:
    size = 0
    for child in node.children.values():
        if child.type == NodeType.DIRECTORY:
            size = size + get_size(child, large_ones)
        else:
            size = size + child.size
    node.size = size
    if size < 100000:
        large_ones.append(node)
    return size


def main():
    cwd = ""
    root_node = Node("/", NodeType.DIRECTORY, dict(), -1)
    tiny_ones = []
    with open("input.txt", "r") as f:
        gen = genlines(f)
        inp = next(gen)
        while inp is not None:
            print("cwd " + cwd)
            print("command " + inp)
            if inp.startswith("$ cd /"):
                cwd = ""
            elif inp.startswith("$ cd .."):
                cwd = "/".join(cwd.split("/")[:-2]) + "/"
                if cwd == "/":
                    cwd = ""
            elif inp.startswith("$ cd "):
                cwd = cwd + inp.replace("$ cd ", "") + "/"
            elif inp.startswith("$ ls"):
                inp = next(gen)
                print("process ls " + inp)
                while inp is not None and not inp.startswith("$"):
                    if inp.startswith("dir "):
                        print("is dir " + inp)
                        dirName = inp.replace("dir ", "")
                        get_node(root_node, cwd).children[dirName] = Node(dirName, NodeType.DIRECTORY, dict(), -1)
                    else:
                        print("is file " + inp)
                        size, name = inp.split(" ")
                        get_node(root_node, cwd).children[name] = Node(name, NodeType.FILE, dict(), int(size))
                    inp = next(gen)
                continue
            else:
                sys.stderr.write("CRITICAL unknown command " + inp)
            inp = next(gen)
        get_size(root_node, tiny_ones)
    ac = 0
    for node in tiny_ones:
        ac += node.size
    print(ac)



if __name__ == "__main__":
    main()
