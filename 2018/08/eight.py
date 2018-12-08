#!/usr/bin/env python
"""
Day 8: Memory Maneuver

Parse a long list of integers into a tree of nodes, then

A. Sum the metadata for every node in the tree
B. Calculate the value of the root node given some stupid rules
"""
class Node:
    def __init__(self):
        self.metadata = []
        self.children = []


def read_node(data):
    node = Node()
    child_count = data.pop(0)
    meta_count = data.pop(0)

    for i in range(child_count):
        data, child = read_node(data)
        node.children.append(child)

    node.metadata = data[:meta_count]
    data = data[meta_count:]  # Remainder after metadata
    return data, node


def sum_metadata(node):
    return sum(node.metadata) + sum(sum_metadata(c) for c in node.children)


def sum_root_node(node):
    if not node.children:
        return sum(node.metadata)
    total = 0
    for idx in node.metadata:
        if idx == 0:  # 0th child index is invalid
            continue
        try:
            child = node.children[idx - 1]  # idx is 1 based
        except IndexError:  # Ignore invalid indices
            continue
        total += sum_root_node(child)
    return total


def main():
    with open('input.txt') as f:
        data = [int(x) for l in f for x in l.strip().split()]

    _, node = read_node(data)
    print('Part A: {} - Sum of metadata'.format(sum_metadata(node)))
    print('Part B: {} - Sum of root node'.format(sum_root_node(node)))


if __name__ == '__main__':
    main()
