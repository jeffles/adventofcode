# coding=utf-8
import copy
import re
import sys
import unittest


class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.neighbors = []
        self.visits = 0
        self.mul_visits = vertex.isupper()

    def add_neighbor(self, neighbor):
        if isinstance(neighbor, Vertex):
            if neighbor.name not in self.neighbors:
                self.neighbors.append(neighbor.name)
                neighbor.neighbors.append(self.name)
                self.neighbors = sorted(self.neighbors)
                neighbor.neighbors = sorted(neighbor.neighbors)
        else:
            return False

    def get_neighbors(self):
        return self.neighbors

    def __repr__(self):
        return str(self.neighbors)

def find_all_paths(graph, start, end, doubled, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start].get_neighbors():
        if node.isupper():
            newpaths = find_all_paths(graph, node, end, doubled, path)
            for newpath in newpaths:
                paths.append(newpath)
        elif node not in path:
            newpaths = find_all_paths(graph, node, end, doubled, path)
            for newpath in newpaths:
                paths.append(newpath)
        #Comment next out for part 1
        elif node != 'start' and not doubled:
            newpaths = find_all_paths(graph, node, end, True, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def part1():
    data = []

    with open('input', 'r') as f:
        for cnt, line in enumerate(f):
            data.append(line.strip().split('-'))

    verts = {}
    for node in data:
        if node[0] not in verts:
            verts[node[0]] = Vertex(node[0])
        if node[1] not in verts:
            verts[node[1]] = Vertex(node[1])
        verts[node[0]].add_neighbor(verts[node[1]])

    print(verts)

    paths = find_all_paths(verts, 'start', 'end', False)
    for path in paths:
        print(path)
    print(len(paths))

    exit()

if __name__ == '__main__':
    # unittest.main()
    part1()
