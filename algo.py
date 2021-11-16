from collections import defaultdict

from enum import Enum


class Action(Enum):
    ENTER = 0
    EXIT = 1


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Graph:
    @staticmethod
    def build_graph(edges):
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
        return graph

    @staticmethod
    def dfs_iter(graph, start):
        cycle_is_present = False
        state = {v: Color.WHITE for v in graph}
        stack = [(Action.ENTER, start)]
        while stack:
            action, v = stack.pop()
            if action == Action.EXIT:
                state[v] = Color.BLACK
            else:
                state[v] = Color.GRAY
                stack.append((Action.EXIT, v))
                for n in graph[v]:
                    try:
                        if state[n] == Color.GRAY:
                            print('cycle: ', n)
                            cycle_is_present = True
                        elif state[n] == Color.WHITE:
                            stack.append((Action.ENTER, n))
                    except KeyError:
                        pass
        return cycle_is_present


if __name__ == '__main__':
    input_file = "in.txt"
    with open(input_file, mode="r") as f:
        n = int(f.readline())
        EDGES = []
        for i in range(n):
            edge = list(map(int, f.readline().split(' ')))
            EDGES.append(edge)
    graph = Graph.build_graph(EDGES)
    Graph.dfs_iter(graph, 0)
