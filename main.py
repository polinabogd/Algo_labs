from collections import defaultdict


class Graph():
    def __init__(self, vertexes):
        self.vertexes = vertexes
        self.graph = defaultdict(list)

    def add_edge(self, edges):
        for x, y in edges:
            self.graph[x].append(y)

    def dfs(self, u, color):
        color[u] = "GRAY"

        for v in self.graph[u]:
            if color[v] == "GRAY":
                print(v, "<-", end=" ")
                return True

            if color[v] == "WHITE" and self.dfs(v, color) == True:
                print(v, "<-", end=" ")
                return True

        color[u] = "BLACK"
        return False

    def is_cyclic(self):
        color = ["WHITE"] * self.vertexes

        for i in range(self.vertexes):
            if color[i] == "WHITE":
                if self.dfs(i, color):
                    return True
        return False


if __name__ == '__main__':
    input_file = "in.txt"
    with open(input_file, mode="r") as f:
        n = int(f.readline())
        edges = []
        g = Graph(n)
        for i in range(n):
            edge = list(map(int, f.readline().split(' ')))
            edges.append(edge)
            g.add_edge(edges)

    print("Cycle starts here" if g.is_cyclic() == True else "Graph doesn't contain cycle")
