class Graph:
    def __init__(self, key):
        self.key = key
        self.edge_list = []
        self.parent = []
        self.rank = []
        self.final = []

    def add_edge(self, u, v, w):
        self.edge_list.append([u, v, w])

    def find_parent(self, node):
        if node == self.parent[node]:
            return node
        return self.find_parent(self.parent[node])

    def kruskal(self):
        sorted_edge_list= sorted(self.edge_list)
        self.parent = [None] * self.key
        self.rank = [None] * self.key

        for node in range(self.key):
            self.parent[node] = node
            self.rank[node] = 0

        for edge in sorted_edge_list:
            root1 = self.find_parent(edge[0])
            root2 = self.find_parent(edge[1])
            if root1 != root2:
                self.final.append(edge)
                if self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                    self.rank[root2] += 1
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1
        cost = 0
        for edge in self.final:
            cost += edge[2]
        return cost


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)
    print("Final weitht of minimum spanning tree : ", end=" ")
    print(g.kruskal())

    print("Vertexes and edges: ")
    for el in g.edge_list:
        print(el, end=" ")
