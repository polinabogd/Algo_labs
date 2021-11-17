from collections import defaultdict


class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def add_edge(self, edges):
        for x, y in edges:
            self.graph[x].append(y)

    def dfs(self, u, color):
        color[u] = "GRAY"

        for v in self.graph[u]:

            if color[v] == "GRAY":
                for k in self.graph.keys():
                    if color[k] == "GRAY":
                        print(k, "->", end=" ")
                return True

            if color[v] == "WHITE" and self.dfs(v, color) == True:
                return True

        color[u] = "BLACK"
        return False

    def is_cyclic(self):
        color = ["WHITE"] * self.V

        for i in range(self.V):
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

    print(" Graph contains cycle" if g.is_cyclic() == True else "Graph doesn't contain cycle")
